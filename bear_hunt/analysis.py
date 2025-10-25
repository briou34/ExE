"""
Usage: analysis.py [--bear {1,2}]
"""

# /// script
# dependencies = [
#     "rich",
#     "pyyaml",
# ]
# ///

import argparse
from collections import defaultdict
from pathlib import Path

import yaml

DAMAGES_LOG = yaml.safe_load((Path(__file__).parent / "damages_log.yml").open("r"))


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
    bear_choice = parser.parse_args().bear
    summary_table = as_rich_table(
        summary(bear=bear_choice),
        columns=["Date", "# Players", "Total score"],
        justifys=[None, "right", "right"],
        title=f"Bear Hunt {bear_choice} - Summary",
    )
    players_table = as_rich_table(
        players_records(bear=bear_choice, n_lasts=7),
        columns=["#", "Player", "Score", "# Hunts"],
        justifys=[None, None, "right", "right"],
        title=f"Bear Hunt {bear_choice} - Top Players over last 7 hunts",
    )
    console.print()
    console.print(summary_table)
    console.print()
    console.print(players_table)


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
                else (
                    ":---:" if j == "center" else ("---:" if j == "right" else ":---")
                )
                for j in justifys
            ]
        )
        + " |"
    )
    rows = [header, separator]
    for row in data:
        rows.append("| " + " | ".join([str(item) for item in row]) + " |")
    return "\n".join(rows)


def score_to_str(score: int) -> str:
    K, M, B = 1_000, 1_000_000, 1_000_000_000
    if score >= B:
        return f"{score / B:.2f}B"
    elif score >= M:
        return f"{score / M:.2f}M"
    elif score >= K:
        return f"{score / K:.2f}K"
    else:
        return str(score)


if __name__ == "__main__":
    main()
