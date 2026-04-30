from process_data.graph_1 import manage_rank_graph
from process_data.graph_2 import manage_stat_graph
from theme import leetcode_palette as palette


def build_graphic(plt, df, username, date_format):
    print(f"        Creating figure with shape: {df.shape}")
    print(f"        Date range for graph: {df['date'].min()} to {df['date'].max()}")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
    fig.patch.set_facecolor(palette["background"])
    print(f"        Figure created, background set to {palette['background']}")

    print(f"        Building rank graph...")
    manage_rank_graph(df, ax1, username)
    print(f"        Rank graph completed")

    print(f"        Building stats graph...")
    manage_stat_graph(df, ax2, date_format)
    print(f"        Stats graph completed")

    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')

    fig.tight_layout()
    print(f"        Figure layout adjusted")
    return fig