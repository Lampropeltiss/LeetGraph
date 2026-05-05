import matplotlib.pyplot as plt
from theme import leetcode_palette as palette


def manage_pie_chart(plt, df, ax):
    # Получаем последние данные
    last_row = df.iloc[-1]

    # Данные для диаграммы
    categories = ['Easy', 'Medium', 'Hard']
    solved_counts = [
        last_row['easy'],
        last_row['medium'],
        last_row['hard']
    ]

    # Цвета для каждой категории из palette
    colors = [palette["easy"], palette["medium"], palette["hard"]]

    explode = [0.01, 0.01, 0.03]

    # Вычисляем проценты для каждого сектора
    total_solved = last_row['total_solved']
    percentages = [count / total_solved * 100 for count in solved_counts]

    # Создаем лейблы в формате 'Easy: 53 tasks (57.6%)'
    custom_labels = [f"{cat}: {pct:.1f}%\n{count:,} tasks"
              for cat, count, pct in zip(categories, solved_counts, percentages)]

    # Создаем круговую диаграмму с уменьшенным радиусом
    wedges, texts = ax.pie(
        solved_counts,
        labels=custom_labels,
        colors=colors,
        startangle=90,
        explode=explode,
        radius=0.2,  # Уменьшаем диаметр (стандарт = 1.0)
        textprops={'fontsize': 16, 'color': palette["text"]}
    )

    ax.axis('equal')

    return ax