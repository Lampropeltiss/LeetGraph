import pandas as pd
from matplotlib.dates import AutoDateLocator, DateFormatter
from matplotlib.ticker import FuncFormatter, MaxNLocator
from theme import leetcode_palette as palette


def manage_stat_graph(df, ax2, date_format):
    ax2.set_facecolor(palette["canvas"])

    width = pd.Timedelta(days=0.4)  # Ширина столбцов

    ax2.bar(df['date'], df['easy_new'],
            width=width,
            color=palette['easy'],
            label='Easy',
            alpha=0.9,
            edgecolor=palette["grid"],
            linewidth=0.5)

    ax2.bar(df['date'], df['medium_new'],
            width=width,
            bottom=df['easy_new'],
            color=palette['medium'],
            label='Medium',
            alpha=0.9,
            edgecolor=palette["grid"],
            linewidth=0.5)

    ax2.bar(df['date'], df['hard_new'],
            width=width,
            bottom=df['easy_new'] + df['medium_new'],
            color=palette['hard'],
            label='Hard',
            alpha=0.9,
            edgecolor=palette["grid"],
            linewidth=0.5)

    # Добавление линии общего количества решенных задач (total_solved)
    ax2_twin = ax2.twinx()
    ax2_twin.plot(df['date'], df['total_solved'],
                  color='#9fa1a4',
                  marker='D',
                  markersize=5,
                  linewidth=2,
                  linestyle='--',
                  alpha=0.8,
                  label='Total Solved (cumulative)')
    ax2_twin.tick_params(colors=palette["text"])
    ax2_twin.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', ' ')))
    ax2_twin.set_ylabel('Total Solved (Cumulative)', color=palette["text"], fontsize=11)

    # Настройки нижнего графика
    ax2.set_title("New Problems Solved Over Time (Stacked Bar Chart)",
                  color=palette["text"],
                  fontsize=18,
                  pad=20,
                  fontweight=500)

    ax2.set_xlabel('Date', color=palette["text"], fontsize=12)
    ax2.set_ylabel('New Problems Solved', color=palette["text"], fontsize=12)
    ax2.tick_params(colors=palette["text"])
    ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'.replace(',', ' ')))

    locator = AutoDateLocator(maxticks=12)
    ax2.xaxis.set_major_locator(locator)

    # Форматирование дат
    formatter = DateFormatter(date_format)
    ax2.xaxis.set_major_formatter(formatter)

    # Настройка границ для нижнего графика
    for spine in ax2.spines.values():
        spine.set_color(palette["grid"])
        spine.set_linewidth(0.5)

    # Настройка границ для правой оси (twin)
    for spine in ax2_twin.spines.values():
        spine.set_color(palette["grid"])
        spine.set_linewidth(0.5)

    # Легенда для гистограммы (левая ось)
    legend2 = ax2.legend(facecolor=palette["legend"],
                         edgecolor=palette["grid"],
                         loc='upper left',
                         prop={'size': 10},
                         ncol=3)
    for text in legend2.get_texts():
        text.set_color(palette["text"])

    # Легенда для линии total_solved (правая ось)
    legend2_twin = ax2_twin.legend(facecolor=palette["legend"],
                                   edgecolor=palette["grid"],
                                   loc='upper right',
                                   bbox_to_anchor=(1.0, 0.8),
                                   prop={'size': 10})
    for text in legend2_twin.get_texts():
        text.set_color(palette["text"])

    return
