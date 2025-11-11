"""
Usage: hive.py [--tilted] [--save] [--show]
"""

# /// script
# dependencies = [
#   "matplotlib",
#   "PyQT6",
#   "pyyaml",
#   "rich",
# ]
# ///

import argparse
from datetime import UTC, datetime
from functools import partial
from pathlib import Path

import yaml

LOCATIONS = yaml.safe_load((Path(__file__).parent / "locations.yml").open("r"))
NAMES_SPLITTING = yaml.safe_load((Path(__file__).parent / "names_splitting.yml").open("r"))

COLORS = {
    "pitfall": "#E95DCD",
    "hq": "#306B34",
    "rsr node": "#F3B700",
    "city": [0.4, 0.8, 1, 0.5],
    "banner": "#F63E02",
    "fortress": [1, 0, 0],
    "mountain": [0, 0, 0],
    "lake": [0.25, 0.86, 0.87],
}

XMIN, XMAX = 706, 742
YMIN, YMAX = 537, 561

# https://www.freefontdownload.org/en/stheiti-regular.font
HEITI_FONT_PATH = Path(__file__).parent / "fonts" / "stheiti-regular.ttf"

# https://fonts.google.com/noto/specimen/Noto+Serif+KR
KOR_FONT_PATH = Path(__file__).parent / "fonts" / "NotoSerifKR-Regular.ttf"

HEITI_NAMES = {
    "CHEN陈",
    "TW拍吉",
    "一代宗师林总",
    "少量課金者",
    "屁屁俠",
    "島鹿小丸子",
    "招財進寶",
    "是17呀",
    "熾夜星空",
    "熾星空",
    "球球仔",
    "趴懶大",
    "達努巴克",
    "黃金海岸",
    "다죽자",
}

KOR_NAMES = {
    "차은아",
    "흐림없는눈",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tilted", action="store_true", help="Use tilted (rotated) axes")
    parser.add_argument(
        "--save",
        action="store_true",
        default=False,
        help="Save the figure instead of showing it",
    )
    parser.add_argument("--show", action="store_true", default=False, help="Show the figure")
    parser.add_argument(
        "--print", action="store_true", default=False, help="Print cities locations table"
    )
    args = parser.parse_args()

    if args.print:
        from rich.console import Console

        console = Console()
        console.print(as_rich_table(get_cities_locations_table(), columns=["Name", "X", "Y"]))

    if args.show or args.save:
        import matplotlib.pyplot as plt

        if args.tilted:
            ax = setup_rotated_ax()  # in game orientation
        else:
            ax = setup_normal_ax()  # easier to move objects when coding
        fig = plot_base_map(
            ax=ax,
            hq_loc=LOCATIONS["hq"],
            pit1_loc=LOCATIONS["pitfall_1"],
            pit2_loc=LOCATIONS["pitfall_2"],
        )
        fig = plot_cities(
            ax=ax,
            cities_locs1=add_deltas(LOCATIONS["pitfall_1"], LOCATIONS["cities"]["bear_1"]),
            cities_locs2=add_deltas(LOCATIONS["pitfall_2"], LOCATIONS["cities"]["bear_2"]),
        )
        if args.show:
            plt.show()
        if args.save:
            imgs_dir = Path(__file__).parent / "images"
            imgs_dir.mkdir(exist_ok=True)
            today_str = datetime.now(tz=UTC).strftime("%Y-%m-%d")
            fig.savefig(imgs_dir / f"{today_str}_hive.png", dpi=200)


def get_cities_locations_table():
    pit1_loc = LOCATIONS["pitfall_1"]
    pit2_loc = LOCATIONS["pitfall_2"]
    cities_locs1 = add_deltas(pit1_loc, LOCATIONS["cities"]["bear_1"])
    cities_locs2 = add_deltas(pit2_loc, LOCATIONS["cities"]["bear_2"])
    cities_locs_table = [
        (name, x, y)
        for name, (x, y) in dict(sorted({**cities_locs1, **cities_locs2}.items())).items()
    ]
    return cities_locs_table


def plot_cities(ax, cities_locs1, cities_locs2):
    import matplotlib.font_manager as fm

    add_build = partial(add_building, ax=ax)
    add_city = partial(
        add_build, width=2, height=2, color=COLORS["city"], text_kwargs={"fontsize": 8}
    )

    heiti_font = fm.FontProperties(fname=HEITI_FONT_PATH)
    kor_font = fm.FontProperties(fname=KOR_FONT_PATH)

    for locs, color in zip([cities_locs1, cities_locs2], ["#50C9CE", "#9883E5"]):
        for name, loc in locs.items():
            text_kwargs = {"fontsize": 7}
            rect_kwargs = {"alpha": 1}

            if (
                name
                in {  # Cities to move
                    # "Briou",
                    # "King of Dogs",
                    # "Willow",
                }
            ):
                rect_kwargs["edgecolor"] = "black"
                rect_kwargs["linewidth"] = 2

            if name in {  # MIA
                "GUNNAR",
            }:
                rect_kwargs["edgecolor"] = "red"
                rect_kwargs["linewidth"] = 2

            if name in HEITI_NAMES:
                text_kwargs["fontproperties"] = heiti_font
            elif name in KOR_NAMES:
                text_kwargs["fontproperties"] = kor_font

            label = name
            if len(label) > 8:
                if label in NAMES_SPLITTING:
                    label = NAMES_SPLITTING[label]
                else:
                    label = "\n".join([label[:8], label[8:16]])

            add_city(
                loc,
                label=label,
                color=color,
                text_kwargs=text_kwargs,
                rect_kwargs=rect_kwargs,
            )
    return ax.figure


def plot_base_map(ax, hq_loc, pit1_loc, pit2_loc):
    from matplotlib.patches import Polygon

    pit1_x, pit1_y = pit1_loc
    pit2_x, pit2_y = pit2_loc

    add_build = partial(add_building, ax=ax)
    add_pitfall = partial(add_build, width=3, height=3, color=COLORS["pitfall"], label="Pitfall")
    add_rsr_node = partial(add_build, width=2, height=2, color=COLORS["rsr node"])

    add_banner = partial(add_banner_, ax=ax, pad=0.2, color=COLORS["banner"])
    add_hq = partial(add_hq_, color=COLORS["hq"], ax=ax)

    # Main buildings
    add_hq(hq_loc)
    add_pitfall(
        (pit1_x, pit1_y),
        label="19:00\nUTC",
        text_kwargs={"fontsize": 14, "fontweight": "bold"},
    )
    add_pitfall(
        (pit2_x, pit2_y),
        label="12:00\nUTC",
        text_kwargs={"fontsize": 14, "fontweight": "bold"},
    )

    # Banners
    for loc in LOCATIONS["banners"]:
        add_banner(loc)

    # Ressource nodes, Mountains, Lakes
    for loc, rsr in LOCATIONS.get("resources_nodes", []):
        # add_rsr_node(loc, label=rsr)
        add_rsr_node(loc)
    for locs in LOCATIONS.get("mountains", []):
        ax.add_patch(Polygon(locs, facecolor=COLORS["mountain"]))
    for locs in LOCATIONS.get("lakes", []):
        ax.add_patch(Polygon(locs, facecolor=COLORS["lake"]))

    # Format figure
    ax.set_xticks(range(XMIN, XMAX + 1, 1))
    for label in ax.get_xticklabels():
        label.set_rotation(90)
        label.set_horizontalalignment("center")
    today_str = datetime.now(tz=UTC).strftime("%Y-%m-%d")
    ax.set_title(today_str, fontsize=16)

    return ax.figure


# --- ADD BUILDINGS


def add_building(
    xy,
    width,
    height,
    *,
    ax,
    color,
    pad=0.2,
    label=None,
    rect_kwargs=None,
    text_kwargs=None,
):
    from matplotlib.patches import Rectangle

    rect_defaults = dict(linewidth=0, facecolor=color)
    text_defaults = dict(ha="center", va="center", fontsize=11, color="black")
    if rect_kwargs is None:
        rect_kwargs = {}
    if text_kwargs is None:
        text_kwargs = {}
    rect_kwargs = {**rect_defaults, **rect_kwargs}
    text_kwargs = {**text_defaults, **text_kwargs}
    x, y = xy
    # Use padding to better see individual buildings
    x += pad
    y += pad
    width -= 2 * pad
    height -= 2 * pad
    rect = Rectangle([x, y], width, height, **rect_kwargs)
    if label:
        ax.text(x + width / 2, y + height / 2, label, **text_kwargs)
    ax.add_patch(rect)


def add_banner_(xy, *, ax, color=None, pad=0.2, **rect_kwargs):
    from matplotlib.patches import Rectangle

    if color is None:
        color = COLORS["banner"]
    add_building(
        xy,
        width=1,
        height=1,
        ax=ax,
        color=color,
        pad=pad,
        label=None,
        rect_kwargs={"zorder": 2, **rect_kwargs},
        text_kwargs={"zorder": 3, "fontsize": 10},
    )
    # Add a 7x7 control area around the banner
    control_area = Rectangle(
        (xy[0] - 3, xy[1] - 3),
        7,
        7,
        linewidth=0,
        edgecolor="black",
        facecolor=[0, 0, 0, 0.15],
        zorder=0,
    )
    ax.add_patch(control_area)


def add_hq_(xy, ax, color=None):
    from matplotlib.patches import Rectangle

    if color is None:
        color = COLORS["hq"]
    add_building(
        xy,
        width=3,
        height=3,
        ax=ax,
        color=color,
        label="HQ",
        text_kwargs={"fontsize": 15, "fontweight": "bold", "zorder": 3},
        rect_kwargs={"zorder": 2},
    )
    # Add a 14x14 control area around the HQ
    control_area = Rectangle(
        (xy[0] - 6, xy[1] - 6),
        15,
        15,
        linewidth=0,
        edgecolor="black",
        facecolor=[0, 0, 0, 0.15],
        zorder=0,
    )
    ax.add_patch(control_area)


# --- SETUP AXES


def setup_normal_ax():
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(14, 10))
    fig.subplots_adjust(left=0.04, right=0.96, top=0.97, bottom=0.03)
    ax.set_xlim(XMIN, XMAX)
    ax.set_ylim(YMIN, YMAX)
    ax.set_aspect("equal")
    ax.set_xticks(range(XMIN, XMAX + 1, 1))
    ax.set_yticks(range(YMIN, YMAX + 1, 1))
    ax.grid(which="both", color="gray", linestyle="--", linewidth=0.5)
    return ax


def setup_rotated_ax():
    import matplotlib.pyplot as plt
    import mpl_toolkits.axisartist.floating_axes as floating_axes
    from matplotlib.transforms import Affine2D
    from mpl_toolkits.axisartist.grid_finder import FixedLocator

    fig = plt.figure(figsize=(10, 10))
    tr = Affine2D().rotate_deg(45)
    grid_helper = floating_axes.GridHelperCurveLinear(
        tr,
        extremes=(XMIN, XMAX, YMIN, YMAX),
        grid_locator1=FixedLocator(range(XMIN, XMAX + 1, 1)),
        grid_locator2=FixedLocator(range(YMIN, YMAX + 1, 1)),
    )
    ax = fig.add_subplot(111, axes_class=floating_axes.FloatingAxes, grid_helper=grid_helper)
    ax.grid(which="both", color="gray", linestyle="--", linewidth=0.5)

    return ax.get_aux_axes(tr)


# --- UTILS


def add_deltas(base_loc, deltas):
    return {name: (base_loc[0] + dx, base_loc[1] + dy) for name, (dx, dy) in deltas.items()}


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
