"""
Usage:

    bear_hunt_prep.py [--ratio INFANTRY CAVALRY ARCHERS]
                       --troops INFANTRY CAVALRY ARCHERS
                       --capacities CAPACITY [CAPACITY ...]

Examples:

    bear_hunt_prep.py --ratio 10 20 70 --troops 199160 193160 199160 --capacities 127190
    bear_hunt_prep.py -r 10 20 70 -t 199160 193160 199160 -c 127190 127190 127190 127190 87600
    bear_hunt_prep.py -t 199160 193160 199160 -c 127190

Output:

                                  Bear Hunt Troop Formation
┏━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┓
┃  Formation  ┃ Infantry ┃ Cavalry ┃ Archers ┃  % Inf ┃  % Cav ┃ % Arch ┃   Total ┃ Capacity ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━┩
│ Formation 1 │   12,719 │  25,438 │  89,033 │ 10.00% │ 20.00% │ 70.00% │ 127,190 │  127,190 │
│ Formation 2 │   12,719 │  25,438 │  89,033 │ 10.00% │ 20.00% │ 70.00% │ 127,190 │  127,190 │
│ Formation 3 │   12,719 │  93,377 │  21,094 │ 10.00% │ 73.42% │ 16.58% │ 127,190 │  127,190 │
│ Formation 4 │   78,283 │  48,907 │       0 │ 61.55% │ 38.45% │  0.00% │ 127,190 │  127,190 │
│ Formation 5 │   82,720 │       0 │       0 │ 94.43% │  0.00% │  0.00% │  82,720 │   87,600 │
├─────────────┼──────────┼─────────┼─────────┼────────┼────────┼────────┼─────────┼──────────┤
│    Total    │  199,160 │ 193,160 │ 199,160 │ 33.67% │ 32.66% │ 33.67% │ 591,480 │  596,360 │
└─────────────┴──────────┴─────────┴─────────┴────────┴────────┴────────┴─────────┴──────────┘
"""

# /// script
# dependencies = [
#   "rich",
# ]
# ///

import argparse
from rich.table import Table
from rich.console import Console


def main():
    console = Console()
    args = process_args()

    ratio = args.ratio
    troops = args.troops
    capacities = args.capacities

    console.print()
    console.print(f"Total Troops: {sum(troops):,d}")
    console.print(f"    Infantry: {troops[0]:,d}")
    console.print(f"     Cavalry: {troops[1]:,d}")
    console.print(f"     Archers: {troops[2]:,d}")

    squads = make_formations(ratio, troops, capacities)
    table = formations_report(squads, capacities)
    console.print(table)


def make_formations(ratio, troops, capacities):
    squads = []
    for capacity in capacities:
        squad = fit_ratio(ratio, troops, capacity)
        squads.append(squad)
        troops = [trps - used for trps, used in zip(troops, squad)]
    return squads


def formations_report(squads, capacities):
    table = Table(title="Bear Hunt Troop Formation")
    table.add_column("Formation", justify="center", style="cyan", no_wrap=True)
    table.add_column("Infantry", justify="right", style="green")
    table.add_column("Cavalry", justify="right", style="yellow")
    table.add_column("Archers", justify="right", style="blue")
    table.add_column("% Inf", justify="right", style="green")
    table.add_column("% Cav", justify="right", style="yellow")
    table.add_column("% Arch", justify="right", style="blue")
    table.add_column("Total", justify="right", style="magenta")
    table.add_column("Capacity", justify="right", style="magenta")

    for i, (squad, capacity) in enumerate(zip(squads, capacities), 1):
        total = sum(squad)
        pcts = [(squad[i] / capacity) * 100 if capacity > 0 else 0 for i in range(3)]
        table.add_row(
            f"Formation {i}",
            f"{squad[0]:,d}",
            f"{squad[1]:,d}",
            f"{squad[2]:,d}",
            f"{pcts[0]:.2f}%",
            f"{pcts[1]:.2f}%",
            f"{pcts[2]:.2f}%",
            f"{total:,d}",
            f"{capacity:,d}",
        )
    table.add_section()
    totals = [sum(squad[i] for squad in squads) for i in range(3)]

    table.add_row(
        "Total",
        f"{totals[0]:,d}",
        f"{totals[1]:,d}",
        f"{totals[2]:,d}",
        f"{totals[0] / sum(totals) * 100:.2f}%",
        f"{totals[1] / sum(totals) * 100:.2f}%",
        f"{totals[2] / sum(totals) * 100:.2f}%",
        f"{sum(totals):,d}",
        f"{sum(capacities):,d}",
    )
    return table


def fit_ratio(ratios, units, capacity):
    """
    Fit units into capacity while maintaining ratios as closely as possible.

    If there is enough units, the capacity is filled according to the ratios.
    If one unit type runs out, the remaining capacity is filled with the other types, even if it skews the ratio.
    Order of priority to fill is archer > cavalry > infantry.
    No more units than available are used.

    Parameters
    ----------
    ratios : tuple of int
        Ratios for infantry, cavalry, and archers in percentage (e.g., (10, 20, 70)).
    units : tuple of int
        Available units for infantry, cavalry, and archers.
    capacity : int
        Total capacity to fill.
    """
    infantry_ratio, cavalry_ratio, archers_ratio = ratios
    infantry_ratio /= 100
    cavalry_ratio /= 100
    archers_ratio /= 100
    total_ratio = infantry_ratio + cavalry_ratio + archers_ratio
    assert total_ratio == 1
    infantry_units, cavalry_units, archers_units = units

    infantry_capacity = int(capacity * infantry_ratio)
    cavalry_capacity = int(capacity * cavalry_ratio)
    archers_capacity = capacity - infantry_capacity - cavalry_capacity
    infantry_used = min(infantry_units, infantry_capacity)
    cavalry_used = min(cavalry_units, cavalry_capacity)
    archers_used = min(archers_units, archers_capacity)
    used_capacity = infantry_used + cavalry_used + archers_used
    remaining_capacity = capacity - used_capacity
    if remaining_capacity > 0:  # Fill remaining capacity with archers first
        additional_archers = min(archers_units - archers_used, remaining_capacity)
        archers_used += additional_archers
        remaining_capacity -= additional_archers
    if remaining_capacity > 0:  # Fill remaining capacity with cavalry next
        additional_cavalry = min(cavalry_units - cavalry_used, remaining_capacity)
        cavalry_used += additional_cavalry
        remaining_capacity -= additional_cavalry
    if remaining_capacity > 0:  # Fill remaining capacity with infantry last
        additional_infantry = min(infantry_units - infantry_used, remaining_capacity)
        infantry_used += additional_infantry
        remaining_capacity -= additional_infantry
    assert infantry_used <= infantry_units
    assert cavalry_used <= cavalry_units
    assert archers_used <= archers_units
    assert infantry_used + cavalry_used + archers_used <= capacity
    return infantry_used, cavalry_used, archers_used


def process_args():
    parser = argparse.ArgumentParser(description="Prepare troop formations for bear hunt event.")
    parser.add_argument(
        "--ratio",
        "-r",
        type=int,
        nargs=3,
        metavar=("INFANTRY", "CAVALRY", "ARCHERS"),
        default=(10, 20, 70),
        help="Troop ratio percentages (default: 10 20 70)",
    )
    parser.add_argument(
        "--troops",
        "-t",
        type=int,
        nargs=3,
        metavar=("INFANTRY", "CAVALRY", "ARCHERS"),
        required=True,
        help="Available troops for infantry, cavalry, and archers.",
    )
    parser.add_argument(
        "--capacities",
        "-c",
        type=int,
        nargs="+",
        metavar="CAPACITY",
        required=True,
        help=(
            "List of formation capacities. If only one capacity is provided, "
            "it will be used for all six formations."
        ),
    )
    args = parser.parse_args()
    if len(args.capacities) == 1:
        args.capacities = args.capacities * 6
    return args


if __name__ == "__main__":
    main()
