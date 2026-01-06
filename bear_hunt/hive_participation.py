# /// script
# dependencies = [
#   "matplotlib",
#   "PyQT6",
#   "pyyaml",
# ]
# ///

import argparse
import sys
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import yaml
from matplotlib.patches import Rectangle

sys.path.append(str(Path(__file__).parent.parent / "hive"))

from hive import (
    HEITI_FONT_PATH,
    HEITI_NAMES,
    KOR_FONT_PATH,
    KOR_NAMES,
    LOCATIONS,
    MOVING,
    NAMES_SPLITTING,
    add_building,
    add_deltas,
    plot_base_map,
    setup_normal_ax,
)

DAMAGES_LOG = yaml.safe_load(
    (Path(__file__).parent / ".." / "bear_hunt" / "damages_log.yml").read_text()
)


def main():
    parser = argparse.ArgumentParser(description="Analyze bear hunt damages.")
    parser.add_argument(
        "--nlasts",
        "-n",
        type=int,
        default=7,
        help="Number of last hunts to consider. Default is 7.",
    )
    parser.add_argument(
        "--moving",
        action="store_true",
        default=False,
        help="Wether generate the map with future cities locations, highlighting them.",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        default=False,
        help="Save the figure instead of showing it.",
    )
    args = parser.parse_args()
    n_lasts = args.nlasts

    # If moving asked, check that we have moving data, or exit
    if args.moving:
        if not MOVING["bear_1"] and not MOVING["bear_2"]:
            print("No moving data available, cannot generate moving map.")
            return

    dates1 = sorted(list(DAMAGES_LOG["bear1"].keys()))[-n_lasts:]
    dates2 = sorted(list(DAMAGES_LOG["bear2"].keys()))[-n_lasts:]
    log_bear1 = [DAMAGES_LOG["bear1"][date] for date in dates1]
    log_bear2 = [DAMAGES_LOG["bear2"][date] for date in dates2]

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

    # Map
    cities_locs = add_deltas(LOCATIONS["pitfall_1"], LOCATIONS["cities"]["bear_1"]) | add_deltas(
        LOCATIONS["pitfall_2"], LOCATIONS["cities"]["bear_2"]
    )
    if args.moving:
        cities_locs_moving = add_deltas(LOCATIONS["pitfall_1"], MOVING["bear_1"]) | add_deltas(
            LOCATIONS["pitfall_2"], MOVING["bear_2"]
        )
    else:
        cities_locs_moving = {}

    ax = setup_normal_ax()
    fig = plot_base_map(
        ax=ax,
        hq_loc=LOCATIONS["hq"],
        pit1_loc=LOCATIONS["pitfall_1"],
        pit2_loc=LOCATIONS["pitfall_2"],
    )

    cmap_bear1 = plt.get_cmap("Purples")
    cmap_bear2 = plt.get_cmap("Greens")
    cmap_both = plt.get_cmap("Oranges")

    # Colors according to participation
    colors = {}
    for player in damages.keys():
        part1, part2 = participations[player]
        if part1 == 0 and part2 == 0:
            # Should never happen, if no participation then not in the logs
            clr = mcolors.to_rgb("#FF0000")
        else:
            if part1 != 0 and part2 == 0:
                cmap = cmap_bear1
            elif part2 != 0 and part1 == 0:
                cmap = cmap_bear2
            else:  # Both bears
                if part1 >= 2.5 * part2:  # Still mostly bear 1
                    cmap = cmap_bear1
                elif part2 >= 2.5 * part1:  # Still mostly bear 2
                    cmap = cmap_bear2
                else:
                    cmap = cmap_both
            clr = cmap((part1 + part2) / n_lasts * 0.8)
        colors[player] = mcolors.to_hex(clr)
    fig = plot_cities_with_participation(
        ax, cities_locs, participations, colors, n_lasts, cities_locs_moving
    )

    start_date = sorted(dates1 + dates2)[0]
    end_date = sorted(dates1 + dates2)[-1]
    ax.set_title(f"Bear Hunt Participation: {start_date} -- {end_date} ({n_lasts} Hunts)")

    # Draw legend
    legend_x = 0.015
    legend_y = 0.955
    legend_spacing = 0.04
    legend_items = [
        ("Mostly Bear 1", cmap_bear1(0.6)),
        ("Mostly Bear 2", cmap_bear2(0.6)),
        ("Both Bears", cmap_both(0.6)),
        ("No Participation", "#FFFFFF"),
    ]
    for i, (label, color) in enumerate(legend_items):
        rect = Rectangle(
            (legend_x, legend_y - i * legend_spacing),
            0.025,
            0.03,
            transform=ax.transAxes,
            color=color,
            ec="black" if label != "No Participation" else "red",
        )
        ax.add_patch(rect)
        ax.text(
            legend_x + 0.035,
            legend_y - i * legend_spacing + 0.015,
            label,
            transform=ax.transAxes,
            va="center",
            fontsize=10,
        )

    if args.save:
        imgs_dir = Path(__file__).parent / "images"
        imgs_dir.mkdir(exist_ok=True)
        today_str = datetime.now(tz=UTC).strftime("%Y-%m-%d")
        if args.moving:
            fpath = imgs_dir / f"{today_str}_hive_participation_moving.png"
        else:
            fpath = imgs_dir / f"{today_str}_hive_participation.png"
        fig.savefig(fpath, dpi=200)
    else:
        plt.show()


def plot_cities_with_participation(
    ax, locations, participations, colors, n, locations_moving=set()
):
    from functools import partial

    import matplotlib.font_manager as fm

    add_build = partial(add_building, ax=ax)
    add_city = partial(add_build, width=2, height=2, text_kwargs={"fontsize": 8})

    heiti_font = fm.FontProperties(fname=HEITI_FONT_PATH)
    kor_font = fm.FontProperties(fname=KOR_FONT_PATH)

    for name, loc in locations.items():
        part1, part2 = participations.get(name, (0, 0))
        if (part1 + part2) >= 0.75 * n:
            text_color = "white"
        else:
            text_color = "black"

        text_kwargs = {"fontsize": 7, "color": text_color}
        rect_kwargs = {"alpha": 1}
        if name in HEITI_NAMES:
            text_kwargs["fontproperties"] = heiti_font
        elif name in KOR_NAMES:
            text_kwargs["fontproperties"] = kor_font

        label = name
        if label in NAMES_SPLITTING:
            label = NAMES_SPLITTING[label]
        elif len(label) > 8:
            label = "\n".join([label[:8], label[8:16]])

        if name in locations_moving:
            rect_kwargs["edgecolor"] = "black"
            rect_kwargs["linewidth"] = 2
            text_kwargs["fontweight"] = "bold"
            loc = locations_moving[name]
        elif name not in colors:  # No participation
            rect_kwargs["edgecolor"] = "red"
            rect_kwargs["linewidth"] = 1

        add_city(
            loc,
            label=label,
            color=colors.get(name, "#FFFFFF"),  # no participation
            text_kwargs=text_kwargs,
            rect_kwargs=rect_kwargs,
        )

        # Add participation numbers
        participation_kwargs = {
            "fontsize": 6,
            "va": "top",
            "fontweight": "bold",
        }
        if part1 > 0:
            ax.text(
                loc[0] + 0.3,
                loc[1] + 1.7,
                str(part1),
                ha="left",
                color=text_color,
                **participation_kwargs,
            )
        if part2 > 0:
            ax.text(
                loc[0] + 1.7,
                loc[1] + 1.7,
                str(part2),
                ha="right",
                color=text_color,
                **participation_kwargs,
            )

    return ax.figure


if __name__ == "__main__":
    main()
