from matplotlib import pyplot as plt

from process_data.data_prepare import prepare_data
from process_data.log_last_data import print_stat
from process_data.data_parser import LeetCodeClient
from process_data.data_saver import append_to_csv
from theme import plt_settings, date_formats
from process_data.create_graph import build_graphic

if __name__ == '__main__':
    leetcode_username = "lampropeltiss"
    data_filepath = 'data/leetcode_ranking.csv'
    output_dir = 'output'

    df = prepare_data(data_filepath)
    print_stat(df, output_dir, date_formats['table'])

    client = LeetCodeClient(leetcode_username)
    stats = client.get_stats()
    append_to_csv(stats, data_filepath)

    plt.rcParams.update(plt_settings)
    fig = build_graphic(plt, df, leetcode_username, date_formats['graph'])

    fig.savefig(f"{output_dir}/leetcode_stat_graph.png", dpi=300, bbox_inches='tight')
    plt.close(fig)
