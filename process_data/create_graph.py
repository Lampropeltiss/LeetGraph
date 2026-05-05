from process_data.graph_1 import manage_rank_graph
from process_data.graph_2 import manage_stat_graph
from process_data.pie_chart import manage_pie_chart
from theme import leetcode_palette as palette


def build_graphics(plt, df, username, date_format):
    print(f"        Creating figure with shape: {df.shape}")
    print(f"        Date range for graph: {df['date'].min()} to {df['date'].max()}")

    fig_1, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
    fig_1.patch.set_facecolor(palette["background"])
    print(f"        Figure created, background set to {palette['background']}")

    print(f"        Building rank graph...")
    manage_rank_graph(df, ax1, username)
    print(f"        Rank graph completed")

    print(f"        Building stats graph...")
    manage_stat_graph(df, ax2, date_format)
    print(f"        Stats graph completed")

    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')

    fig_1.tight_layout()
    print(f"        Figure layout adjusted")

    fig_2, ax_pie = plt.subplots(figsize=(10, 8))
    fig_2.patch.set_facecolor(palette["background"])
    manage_pie_chart(plt, df, ax_pie)

    return fig_1, fig_2