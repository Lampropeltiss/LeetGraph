from datetime import datetime
import requests


class LeetCodeClient:
    def __init__(self, username):
        self.username = username
        self.url = "https://leetcode.com/graphql"

    def send_query(self):
        query = """
        query getUserProfile($username: String!) {
          matchedUser(username: $username) {
            profile {
              ranking
            }
            submitStats {
              acSubmissionNum {
                difficulty
                count
              }
            }
          }
        }
        """

        response = requests.post(
            self.url,
            json={"query": query, "variables": {"username": self.username}},
            headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            user_data = data.get('data', {}).get('matchedUser')
            if user_data:
                return user_data
        return None

    def get_stats(self):
        user_data = self.send_query()
        stats = {
            'date'        : datetime.now().strftime('%Y-%m-%d'),
            'rank'        : user_data['profile']['ranking'],
            'easy'        : next(
                (item['count'] for item in user_data['submitStats']['acSubmissionNum']
                 if item['difficulty'] == 'Easy'), 0
            ),
            'medium'      : next(
                (item['count'] for item in user_data['submitStats']['acSubmissionNum']
                 if item['difficulty'] == 'Medium'), 0
            ),
            'hard'        : next(
                (item['count'] for item in user_data['submitStats']['acSubmissionNum']
                 if item['difficulty'] == 'Hard'), 0
            ),
            'total_solved': next(
                (item['count'] for item in user_data['submitStats']['acSubmissionNum']
                 if item['difficulty'] == 'All'), 0
            )
        }
        return stats


if __name__ == '__main__':
    client = LeetCodeClient("lampropeltiss")
    print(client.get_stats())
