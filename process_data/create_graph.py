from process_data.graph_1 import manage_rank_graph
from process_data.graph_2 import manage_stat_graph
from theme import leetcode_palette as palette


def build_graphic(plt, df, username, date_format):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
    fig.patch.set_facecolor(palette["background"])

    manage_rank_graph(df, ax1, username)
    manage_stat_graph(df, ax2, date_format)

    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')

    fig.tight_layout()
    return fig