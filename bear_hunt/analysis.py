"""
Usage: analysis.py [--bear {1,2}]
"""

# /// script
# dependencies = [
#     "rich",
#     "pyyaml",
#     "matplotlib",
#     "PyQT6",
# ]
# ///

import argparse
from collections import defaultdict
from datetime import datetime, timedelta, UTC
from itertools import groupby
from pathlib import Path

import yaml

DAMAGES_LOG = yaml.safe_load((Path(__file__).parent / "damages_log.yml").read_text())


def main():
    from rich.console import Console

    console = Console()

    parser = argparse.ArgumentParser(description="Analyze bear hunt damages.")
    parser.add_argument(
        "--bear",
        "-b",
        type=int,
        choices=[1, 2],
        default=1,
        help="Which bear hunt to analyze (1 or 2). Default is 1.",
    )
    parser.add_argument(
        "--nlasts",
        "-n",
        type=int,
        default=7,
        help="Number of last hunts to consider for player rankings. Default is 7.",
    )
    parser.add_argument(
        "--graph",
        "-g",
        action="store_true",
        default=False,
        help="Display a bar chart of total damages over time.",
    )
    parser.add_argument(
        "--save",
        "-s",
        action="store_true",
        default=False,
        help="Save the graph to a file instead of displaying it.",
    )
    args = parser.parse_args()
    bear_choice = args.bear
    n_lasts = args.nlasts
    summary_table = as_rich_table(
        summary(bear=bear_choice),
        columns=["Date", "# Players", "Total score"],
        justifys=[None, "right", "right"],
        title=f"Bear Hunt {bear_choice} - Summary",
    )
    players_table = as_rich_table(
        players_records(bear=bear_choice, n_lasts=n_lasts),
        columns=["#", "Player", "Score", "# Hunts"],
        justifys=[None, None, "right", "right"],
        title=f"Bear Hunt {bear_choice} - Top Players over last {n_lasts} hunts",
    )
    console.print()
    console.print(summary_table)
    console.print()
    console.print(players_table)

    if args.graph:
        import matplotlib.dates as mdates
        import matplotlib.pyplot as plt
        import matplotlib.ticker as ticker
        from itertools import accumulate

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.set_title(f"Bear Hunt {bear_choice} - Total Damages")

        log = DAMAGES_LOG[f"bear{bear_choice}"]
        # Bar graph
        for date in sorted(list(log.keys())):
            records = sorted(log[date].items(), key=lambda item: item[1], reverse=True)
            players, scores = zip(*records)
            date = datetime.strptime(date, "%Y-%m-%d")
            ax.bar(
                [date] * len(players),
                scores,
                bottom=list(accumulate([0] + list(scores[:-1]))),
                color=["#104956" if i % 2 == 0 else "#1C849B" for i in range(len(players))],
                width=timedelta(days=1.6),
            )

        # Values on top of the bars
        total_scores = [sum(log[date].values()) for date in sorted(list(log.keys()))]
        max_score = max(total_scores)
        ax.set_ylim(0, max_score * 1.1)
        for date, total_score in zip(sorted(list(log.keys())), total_scores):
            color = "darkred" if total_score == max_score else "black"
            ax.text(
                datetime.strptime(date, "%Y-%m-%d"),
                total_score + max_score * 0.015,
                score_to_str(total_score, precision=1)[:-1],
                ha="center",
                va="bottom",
                fontsize=9,
                color=color,
                rotation=90,
            )

        # Set the y-axis ticks in multiples of 2B
        ax.yaxis.set_major_locator(ticker.MultipleLocator(2_000_000_000))
        ax.yaxis.set_major_formatter(
            ticker.FuncFormatter(lambda x, pos: score_to_str(int(x), precision=0))
        )

        # X-axis formatting
        tick_dates = [  # all dates
            datetime.strptime(date, "%Y-%m-%d") for date in sorted(list(log.keys()))
        ][::-1][::2][::-1]

        # Find the middle date for each month to center the label
        month_centers = []
        month_labels = []

        for _, group in groupby(tick_dates, key=lambda d: (d.year, d.month)):
            group = list(group)
            center_date = group[0] + (group[-1] - group[0]) / 2
            month_centers.append(center_date)
            month_labels.append(center_date.strftime("%b %Y"))

        # Add the month labels as a second row of text
        for center, label in zip(month_centers, month_labels):
            ax.annotate(
                label,
                xy=(center, 0),
                xycoords=("data", "axes fraction"),
                xytext=(0, -35),
                textcoords="offset points",
                va="top",
                ha="center",
                fontsize=10,
                fontweight="bold",
            )

        ax.set_xticks(tick_dates)
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d"))
        # ax.tick_params("x", rotation=35)
        # plt.setp(ax.get_xticklabels(), rotation_mode="anchor", ha="right")
        for tick in ax.get_xticklabels():
            tick.set_fontsize(9)

        plt.tight_layout()

        if args.save:
            today_str = datetime.now(tz=UTC).strftime("%Y-%m-%d")
            imgs_dir = Path(__file__).parent / "images"
            imgs_dir.mkdir(exist_ok=True)
            fig.savefig(imgs_dir / f"{today_str}_bear{bear_choice}_damages.png", dpi=200)
        else:
            plt.show()


def summary(bear=1):
    """
    Returns a list of lists [[date, number_of_players, total_score], ...] for
    the given bear hunt.
    """
    log = DAMAGES_LOG[f"bear{bear}"]
    table = []
    for date in sorted(list(log.keys())):
        participants = len(log[date])
        total_score = sum(log[date].values())
        table.append([date, participants, total_score])
    table = [
        [date, str(participants), score_to_str(total_score)]
        for date, participants, total_score in table
    ]
    return table


def players_records(
    bear=1,
    n_lasts=7,  # 7 hunts in between 2 castle fights
):
    log = DAMAGES_LOG[f"bear{bear}"]
    n_lasts = min(n_lasts, len(log))
    log = [log[date] for date in sorted(list(log.keys()))[-n_lasts:]]
    records = defaultdict(int)
    # Sum scores and count participations
    for record in log:
        for player, score in record.items():
            player_record = records.setdefault(player, [0, 0])
            player_record[0] += score  # total score
            player_record[1] += 1  # number of hunts
    # Into a sorted list[tuple[player, score, hunts], ...]
    records = sorted(
        [(player, score, hunts) for (player, (score, hunts)) in records.items()],
        key=lambda item: item[1],
        reverse=True,
    )
    # Add position and format score
    return [
        (pos, player, score_to_str(score), hunts)
        for pos, (player, score, hunts) in enumerate(records, 1)
    ]


def as_rich_table(data, columns, justifys=None, title=None):
    """Generic function to convert data to a rich table."""
    from rich.table import Table

    if justifys is None:
        justifys = [None] * len(columns)
    table = Table(title=title, show_header=True, header_style=None)
    for col, justify in zip(columns, justifys):
        table.add_column(col, justify=justify)
    for row in data:
        table.add_row(*[str(item) for item in row])
    return table


def as_markdown_table(data, columns, justifys=None):
    """Generic function to convert data to a markdown table."""
    if justifys is None:
        justifys = [None] * len(columns)
    # Header
    header = "| " + " | ".join(columns) + " |"
    separator = (
        "| "
        + " | ".join(
            [
                "---"
                if j is None
                else (":---:" if j == "center" else ("---:" if j == "right" else ":---"))
                for j in justifys
            ]
        )
        + " |"
    )
    rows = [header, separator]
    for row in data:
        rows.append("| " + " | ".join([str(item) for item in row]) + " |")
    return "\n".join(rows)


def score_to_str(score: int, precision=2) -> str:
    K, M, B = 1_000, 1_000_000, 1_000_000_000
    if score >= B:
        return f"{score / B:.{precision}f}B"
    elif score >= M:
        return f"{score / M:.{precision}f}M"
    elif score >= K:
        return f"{score / K:.{precision}f}K"
    else:
        return str(score)


if __name__ == "__main__":
    main()
