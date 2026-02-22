"""
Usage: player_history.py <player_name>
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
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import yaml
from rich.console import Console

console = Console()
DAMAGES_LOG = yaml.safe_load(
    (Path(__file__).parent.parent / "bear_hunt" / "damages_log.yml").read_text()
)


def main():

    parser = argparse.ArgumentParser(description="Analyze bear hunt damages for a specific player.")
    parser.add_argument(
        "player_name",
        type=str,
        help="Name of the player to analyze.",
    )
    args = parser.parse_args()

    player_name = args.player_name

    # Filter damages for the specified player
    bear_1_player_damages = [
        (d, record[player_name], 1)
        for d, record in DAMAGES_LOG["bear1"].items()
        if player_name in record
    ]
    bear_2_player_damages = [
        (d, record[player_name], 2)
        for d, record in DAMAGES_LOG["bear2"].items()
        if player_name in record
    ]
    player_damages = sorted(bear_1_player_damages + bear_2_player_damages)

    if not player_damages:
        console.print(f"No damage records found for player '{player_name}'.", style="red")
        return

    # REPORT
    bear_1_count = sum(1 for _, _, bear in player_damages if bear == 1)
    bear_2_count = sum(1 for _, _, bear in player_damages if bear == 2)
    max_damage_date, max_damage, max_damage_bear = max(player_damages, key=lambda x: x[1])
    console.print(f"Bear 1: {bear_1_count} participations.")
    console.print(f"Bear 2: {bear_2_count} participations.")
    console.print(
        f"Maximum damage: {score_to_str(max_damage)} on {max_damage_date} against bear {max_damage_bear}."
    )

    # GRAPH
    dates = [datetime.fromisoformat(d) for d, _, _ in player_damages]
    damages = [damage for _, damage, _ in player_damages]
    cmap = {1: "#8683BD", 2: "#4BB062"}
    colors = [cmap[b] for _, _, b in player_damages]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, damages, marker="none", c="gray")
    ax.scatter(dates, damages, c=colors, s=70, ec="none", zorder=5)
    ax.set_title(f"Damage History for {player_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Damage")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: score_to_str(int(x))))
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    # add horizontal lines for rewards_thresholds
    M = 1_000_000
    B = 1_000_000_000
    rewards_thresholds = [
        8.9 * M,
        20.5 * M,
        47 * M,
        90 * M,
        175 * M,
        330 * M,
        635 * M,
        1.2 * B,
        2.4 * B,
        4.8 * B,
        9.6 * B,
        19.2 * B,
        38.4 * B,
    ]
    max_damage = max(damages)
    # only a few ones below max score and the one above it
    thresholds_to_show = [t for t in rewards_thresholds if t <= max_damage * 1.5][-5:]
    for threshold in thresholds_to_show:
        ax.axhline(threshold, color="orange", linestyle="--", linewidth=0.8)
        ax.text(
            0.999,
            threshold,
            score_to_str(int(threshold), precision=1),
            va="bottom",
            ha="right",
            color="orange",
            fontsize=8,
            transform=ax.get_yaxis_transform(),
        )
    plt.show()


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
