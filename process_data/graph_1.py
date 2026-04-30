from matplotlib.ticker import MaxNLocator, FuncFormatter
from theme import leetcode_palette as palette


def format_large_numbers(x, _):
    x = int(round(x))
    return f'{x:,}'.replace(',', ' ')


def manage_rank_graph(df, ax1, username):
    ax1.set_facecolor(palette["canvas"])

    # Статистика для guide линий
    best_rank = df['rank'].min()
    current_rank = df['rank'].iloc[-1]

    # Удаляем строки с NaN для построения непрерывной линии
    df_rank_clean = df.dropna(subset=['rank'])

    ax1.plot(df_rank_clean['date'], df_rank_clean['rank'],
             color=palette["accent"],
             marker='o',
             markersize=6,
             linewidth=2,
             markerfacecolor=palette["points"],
             markeredgecolor=palette["points"],
             label='Rank')

    # Добавление guide линий
    ax1.axhline(y=best_rank,
                color=palette["max"],
                linestyle=':',
                linewidth=1.5,
                alpha=0.7,
                label=f'Best: {format_large_numbers(best_rank, None)}')

    ax1.axhline(y=current_rank,
                color=palette["accent"],
                linestyle='--',
                linewidth=1.5,
                alpha=0.7,
                label=f'Last: {format_large_numbers(current_rank, None)}')

    # Настройки верхнего графика
    ax1.set_title(f"LeetCode Rank Progression for {username}",
                  color=palette["text"],
                  fontsize=18,
                  pad=20,
                  fontweight=500)

    ax1.set_ylabel('Rank', color=palette["text"], fontsize=12)
    ax1.grid(True, color=palette["grid"], linestyle='-', alpha=0.3)
    ax1.tick_params(colors=palette["text"])
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.yaxis.set_major_formatter(FuncFormatter(format_large_numbers))
    ax1.invert_yaxis()  # Переворачиваем ось ранга

    # Вертикальные линии от точек до оси X (только для существующих точек)
    ax1.vlines(x=df_rank_clean['date'],
               ymin=df_rank_clean['rank'].max(),
               ymax=df_rank_clean['rank'],
               color=palette["guide"],
               alpha=0.3,
               linewidth=0.5)

    # Легенда для верхнего графика
    legend1 = ax1.legend(facecolor=palette["legend"],
                         edgecolor=palette["grid"],
                         loc='upper right',
                         bbox_to_anchor=(1.0, 0.8),
                         prop={'size': 10})
    for text in legend1.get_texts():
        text.set_color(palette["text"])

    # Настройка границ для верхнего графика
    for spine in ax1.spines.values():
        spine.set_color(palette["grid"])
        spine.set_linewidth(0.5)

    return
