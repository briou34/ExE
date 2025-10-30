# /// script
# dependencies = [
#   "matplotlib",
#   "PyQT6",
#   "pyyaml",
#   "rich",
# ]
# ///


import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

import yaml

from collections import defaultdict

DAMAGES_LOG = yaml.safe_load((Path(__file__).parent / "damages_log.yml").open("r"))


def main():
    n_lasts = 7

    # 1. Load the log data
    # 2. Process it so I have for each player the damage per bear number over the last N hunts
    # Need to keep participation also, so I can make a ratio of damage/participation
    # Plot on the map with colors according to ratio and participation as text top right #1/#2

    # Last N hunts for each bear
    log_bear1 = [
        DAMAGES_LOG["bear1"][date]
        for date in sorted(list(DAMAGES_LOG["bear1"].keys()))[-n_lasts:]
    ]
    log_bear2 = [
        DAMAGES_LOG["bear2"][date]
        for date in sorted(list(DAMAGES_LOG[f"bear2"].keys()))[-n_lasts:]
    ]

    participations = defaultdict(lambda: [0, 0])  # bear1, bear2
    damages = defaultdict(lambda: [0, 0])  # bear1, bear2
    for hunt in log_bear1:
        for player, score in hunt.items():
            participations[player][0] += 1
            damages[player][0] += score
    for hunt in log_bear2:
        for player, score in hunt.items():
            participations[player][1] += 1
            damages[player][1] += score

    from rich import print

    print(participations)
    print(damages)


def test_shades():
    # Draw 20 rectangle side by side in a line

    fig, ax = plt.subplots(figsize=(10, 2))

    for i, shade in enumerate(generate_shades("blue", n=20, lighten=True, factor=0.7)):
        rect = Rectangle((i, 0), 0.9, 0.9, facecolor=shade, edgecolor="black")
        ax.add_patch(rect)

    ax.set_xlim(-0.5, 20.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_aspect("equal")

    plt.show()


def generate_shades(color, n=5, lighten=True, factor=1):
    """
    Generate multiple lighter or darker shades of a given color.

    Parameters:
    -----------
    color : str or tuple
        The base color (can be a named color, hex code, or RGB tuple).
    n : int
        Number of shades to generate.
    lighten : bool
        If True, generates lighter shades. If False, generates darker shades.
    factor : float
        The intensity factor for lightening or darkening.

    Returns:
    --------
    list of str
        List of hex color strings representing the shades.
    """
    base = np.array(mcolors.to_rgb(color))
    shades = []

    for i in range(n):
        t = i / (n - 1) * factor
        if lighten:
            new_color = base + (1 - base) * t
        else:
            new_color = base * (1 - t)
        new_color = np.clip(new_color, 0, 1)
        shades.append(mcolors.to_hex(new_color))

    return shades


# def clip(value, min_value=0, max_value=1):
#     return max(min_value, min(value, max_value))

if __name__ == "__main__":
    main()
