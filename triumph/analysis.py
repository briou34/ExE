# /// script
# dependencies = [
#     "rich",
#     "pyyaml",
#     "matplotlib",
#     "PyQT6",
# ]
# ///

import argparse
from pathlib import Path

import yaml

TRIUMPH_LOG = yaml.safe_load((Path(__file__).parent / "triumph_log.yml").open("r"))
TRIUMPH_LOG = dict(sorted(TRIUMPH_LOG.items()))


def main():
    parser = argparse.ArgumentParser(description="Analyze triumph logs.")
    parser.add_argument(
        "--nlasts",
        "-n",
        type=int,
        default=4,
        help="Number of weeks to consider for player rankings. Default is 4.",
    )
    group_fmt = parser.add_mutually_exclusive_group()
    group_fmt.add_argument(
        "--markdown",
        "-m",
        action="store_true",
        default=False,
        help="Output the summary table in markdown format.",
    )
    args = parser.parse_args()

    # Keep only the last n weeks
    n_lasts = args.nlasts
    table_columns, table_rows = summary(n_lasts)
    table_justifys = [None] + ["right"] * len(table_columns[1:])

    if args.markdown:
        summary_table_md = as_markdown_table(
            table_rows, columns=table_columns, justifys=table_justifys
        )
        print(summary_table_md)
    else:
        from rich.console import Console

        console = Console()
        summary_table = as_rich_table(table_rows, columns=table_columns, justifys=table_justifys)
        console.print(summary_table)


def summary(n_lasts):
    weeks = list(TRIUMPH_LOG.keys())[-n_lasts:]
    log = {week: TRIUMPH_LOG[week] for week in weeks}

    # Sum the total points per player
    total_points = {}
    for week, data in log.items():
        for player, points in data.items():
            total_points[player] = total_points.get(player, 0) + points

    # Sort players by total points
    total_points = dict(sorted(total_points.items(), key=lambda item: item[1], reverse=True))

    columns = ["Player", "Total Points", *list(log.keys())]
    rows = [
        (player, points, *[data.get(player, 0) for data in log.values()])
        for player, points in total_points.items()
    ]
    return columns, rows


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


if __name__ == "__main__":
    main()
