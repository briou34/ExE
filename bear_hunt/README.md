# 🐻 Bear Hunt

Keeping only the last 7 records, which is the number of bear hunts in between two Castle Battles.

## Participation

<!-- [[[cog
# Display the latest hive participation map
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_hive_participation\.png")
imgs_dir = Path("bear_hunt", "images")
map_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![Bear Participation]({Path('images') / map_fpath.name})")
]]] -->

![Bear Participation](images/2026-03-13_hive_participation.png)

<!-- [[[end]]] -->

<!-- [[[cog
# Display the future hive participation map once cities start moving
import re
from pathlib import Path
import yaml

MOVING = yaml.safe_load(Path("hive", "locations_moving.yml").read_text())
if MOVING["bear_1"] or MOVING["bear_2"]: # Else, no moving cities, skip
  pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_hive_participation_moving\.png")
  imgs_dir = Path("bear_hunt", "images")
  map_fpath = sorted(
    [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
  )[-1]

  print("\n## Future hive\n")
  print(f"![Bear Participation]({Path('images') / map_fpath.name})")
  print()
]]] -->

## Future hive

![Bear Participation](images/2026-03-13_hive_participation_moving.png)

<!-- [[[end]]] -->

## Bear 1

<!-- [[[cog
# Display the latest bear damages bar graph
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_bear1_damages\.png")
imgs_dir = Path("bear_hunt", "images")
map_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![Bear 1 damages graph]({Path('images') / map_fpath.name})")
]]] -->

![Bear 1 damages graph](images/2026-03-13_bear1_damages.png)

<!-- [[[end]]] -->

<details>
<summary>Table</summary>
<!-- [[[cog
from analysis import summary, as_markdown_table
print()
print(
  as_markdown_table(
    summary(bear=1),
    columns=["Date", "# Players", "Total score"],
    justifys=["left", "right", "right"],
  )
)
]]] -->

| Date       | # Players | Total score |
| :--------- | --------: | ----------: |
| 2025-10-12 |        30 |       5.97B |
| 2025-10-14 |        27 |       4.86B |
| 2025-10-16 |        24 |       3.05B |
| 2025-10-18 |        20 |       2.75B |
| 2025-10-20 |        23 |       3.82B |
| 2025-10-22 |        28 |       6.03B |
| 2025-10-24 |        23 |       5.23B |
| 2025-10-26 |        27 |       4.62B |
| 2025-10-28 |        23 |       3.59B |
| 2025-10-30 |        25 |       6.28B |
| 2025-11-01 |        23 |       6.21B |
| 2025-11-03 |        29 |       5.64B |
| 2025-11-05 |        19 |       5.65B |
| 2025-11-07 |        25 |       9.76B |
| 2025-11-09 |        17 |       8.88B |
| 2025-11-11 |        16 |       9.25B |
| 2025-11-13 |        25 |      11.07B |
| 2025-11-15 |        21 |       6.76B |
| 2025-11-17 |        15 |       6.54B |
| 2025-11-19 |        23 |       7.79B |
| 2025-11-21 |        19 |       7.99B |
| 2025-11-23 |        21 |      10.99B |
| 2025-11-25 |        19 |      10.57B |
| 2025-11-27 |        21 |       8.44B |
| 2025-11-29 |        22 |      13.60B |
| 2025-12-01 |        19 |       8.85B |
| 2025-12-03 |        22 |      13.01B |
| 2025-12-05 |        23 |       8.24B |
| 2025-12-07 |        21 |       8.31B |
| 2025-12-09 |        25 |      17.45B |
| 2025-12-11 |        19 |       6.97B |
| 2025-12-13 |        23 |      16.67B |
| 2025-12-15 |        14 |       7.89B |
| 2025-12-17 |        22 |      15.84B |
| 2025-12-19 |        22 |      17.60B |
| 2025-12-21 |        25 |      11.54B |
| 2025-12-23 |        26 |      14.94B |
| 2025-12-25 |         1 |           0 |
| 2025-12-27 |        24 |      24.08B |
| 2025-12-29 |        27 |      17.31B |
| 2025-12-31 |        15 |       4.81B |
| 2026-01-02 |        20 |      17.32B |
| 2026-01-04 |        19 |      14.51B |
| 2026-01-06 |        25 |      19.03B |
| 2026-01-08 |        32 |      17.52B |
| 2026-01-10 |        29 |      24.69B |
| 2026-01-12 |        29 |      21.75B |
| 2026-01-14 |        34 |      19.80B |
| 2026-01-16 |        24 |      22.52B |
| 2026-01-18 |        30 |      27.45B |
| 2026-01-20 |        33 |      22.92B |
| 2026-01-22 |        30 |      22.36B |
| 2026-01-24 |        28 |      24.59B |
| 2026-01-26 |        34 |      25.50B |
| 2026-01-28 |        35 |      26.25B |
| 2026-01-30 |        29 |      30.00B |
| 2026-02-01 |        35 |      38.71B |
| 2026-02-03 |        32 |      31.02B |
| 2026-02-05 |        29 |      32.84B |
| 2026-02-07 |        26 |      26.56B |
| 2026-02-09 |        26 |      25.05B |
| 2026-02-11 |        30 |      31.04B |
| 2026-02-13 |        23 |      23.31B |
| 2026-02-15 |        34 |      35.47B |
| 2026-02-17 |        30 |      30.10B |
| 2026-02-19 |        21 |      25.60B |
| 2026-02-21 |        29 |      31.13B |
| 2026-02-23 |        29 |      36.50B |
| 2026-02-25 |        29 |      28.13B |
| 2026-02-27 |        27 |      32.93B |
| 2026-03-01 |        31 |      52.94B |
| 2026-03-03 |        31 |      43.74B |
| 2026-03-05 |        29 |      34.73B |
| 2026-03-07 |        27 |      47.24B |
| 2026-03-09 |        30 |      44.19B |
| 2026-03-11 |        31 |      45.95B |
| 2026-03-13 |        22 |      33.26B |

<!-- [[[end]]] -->

</details>

<details>
<summary>Top Players over last 7 hunts</summary>
<!-- [[[cog
from analysis import players_records, as_markdown_table
print()
print(
  as_markdown_table(
    players_records(bear=1, n_lasts=7),
    columns=["#", "Player", "Score", "# Hunts"],
    justifys=["right", "left", "right", "right"],
  )
)
]]] -->

|   # | Player          |   Score | # Hunts |
| --: | :-------------- | ------: | ------: |
|   1 | Paerdekop       |  18.01B |       7 |
|   2 | Sjefen          |  17.76B |       7 |
|   3 | Shell2y         |  15.47B |       7 |
|   4 | Lyghtz          |  15.45B |       7 |
|   5 | Llyod Frontera  |  15.34B |       7 |
|   6 | Coma            |  13.41B |       5 |
|   7 | AZIZ            |  13.34B |       7 |
|   8 | FallingRegrets  |  13.29B |       7 |
|   9 | LadyLove        |  13.27B |       7 |
|  10 | Cery            |  12.96B |       7 |
|  11 | Kenz            |  12.22B |       6 |
|  12 | Briou           |  12.12B |       7 |
|  13 | DarkPanda       |  11.79B |       7 |
|  14 | JoeyBootzz      |  11.55B |       7 |
|  15 | KESHKERES       |   9.53B |       5 |
|  16 | LEA             |   8.55B |       5 |
|  17 | Troka           |   8.16B |       5 |
|  18 | PapiChurro      |   6.98B |       4 |
|  19 | Saint Xitar     |   6.36B |       4 |
|  20 | Sir Bishop      |   5.79B |       6 |
|  21 | EmmyLou         |   5.63B |       5 |
|  22 | Helzu           |   4.60B |       4 |
|  23 | Lord Adoniran   |   4.33B |       4 |
|  24 | Kay_forshort    |   4.22B |       6 |
|  25 | Ellie Softpaw   |   3.97B |       4 |
|  26 | DeathAmongstUs  |   3.71B |       4 |
|  27 | Ocram           |   3.38B |       2 |
|  28 | Frinkley        |   2.96B |       1 |
|  29 | CravenMoorehead |   2.91B |       3 |
|  30 | IrotRiot        |   2.51B |       2 |
|  31 | M E D U S A     |   2.22B |       2 |
|  32 | 帕殿咚          |   1.96B |       3 |
|  33 | Malideiter      |   1.84B |       1 |
|  34 | Donald Porpoise |   1.84B |       5 |
|  35 | Kenpachi        |   1.54B |       1 |
|  36 | Shadow          |   1.53B |       1 |
|  37 | Brica           |   1.46B |       1 |
|  38 | Lagertha        |   1.40B |       2 |
|  39 | mary            |   1.30B |       2 |
|  40 | Diablo          | 982.14M |       3 |
|  41 | Lord_DJ         | 946.90M |       1 |
|  42 | Queen of Hearts | 917.80M |       1 |
|  43 | LightsOutL      | 896.36M |       2 |
|  44 | Trimute         | 857.12M |       2 |
|  45 | SARAH           | 553.01M |       2 |
|  46 | Morphose        | 520.59M |       1 |
|  47 | scorpion        | 416.19M |       1 |
|  48 | Cavendish       | 273.10M |       1 |
|  49 | King Koopa      | 271.50M |       1 |
|  50 | yacob           | 254.48M |       1 |
|  51 | CiusPorpoise    | 136.96M |       1 |
|  52 | O D I N         | 131.06M |       1 |
|  53 | George Floyd    | 125.15M |       5 |
|  54 | LordGiga        | 119.08M |       1 |

<!-- [[[end]]] -->

</details>

## Bear 2

<!-- [[[cog
# Display the latest bear damages bar graph
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_bear2_damages\.png")
imgs_dir = Path("bear_hunt", "images")
graph_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![Bear 2 damages graph]({Path('images') / graph_fpath.name})")
]]] -->

![Bear 2 damages graph](images/2026-03-13_bear2_damages.png)

<!-- [[[end]]] -->

<details>
<summary>Table</summary>
<!-- [[[cog
from analysis import summary, as_markdown_table
print()
print(
  as_markdown_table(
    summary(bear=2),
    columns=["Date", "# Players", "Total score"],
    justifys=["left", "right", "right"],
  )
)
]]] -->

| Date       | # Players | Total score |
| :--------- | --------: | ----------: |
| 2025-10-12 |        22 |       5.53B |
| 2025-10-14 |        24 |       7.03B |
| 2025-10-17 |        25 |       5.54B |
| 2025-10-19 |        23 |       9.44B |
| 2025-10-21 |        28 |      10.03B |
| 2025-10-23 |        28 |       7.12B |
| 2025-10-26 |        18 |       7.66B |
| 2025-10-28 |        24 |       6.57B |
| 2025-10-30 |        24 |       7.36B |
| 2025-11-01 |        22 |       6.04B |
| 2025-11-03 |        23 |       6.58B |
| 2025-11-05 |        32 |       9.16B |
| 2025-11-07 |        21 |       6.61B |
| 2025-11-09 |        20 |      12.90B |
| 2025-11-11 |        25 |       8.72B |
| 2025-11-13 |        27 |      13.60B |
| 2025-11-15 |        28 |      15.08B |
| 2025-11-17 |        21 |      12.78B |
| 2025-11-19 |        24 |      13.25B |
| 2025-11-21 |        22 |       9.94B |
| 2025-11-23 |        20 |      16.66B |
| 2025-11-25 |        21 |       6.60B |
| 2025-11-27 |        23 |       9.68B |
| 2025-11-29 |        21 |      12.44B |
| 2025-12-01 |        23 |      15.88B |
| 2025-12-03 |        20 |       8.04B |
| 2025-12-05 |        21 |      16.37B |
| 2025-12-07 |        16 |      15.28B |
| 2025-12-09 |        24 |      16.47B |
| 2025-12-11 |        20 |      19.59B |
| 2025-12-13 |        19 |       4.30B |
| 2025-12-15 |        21 |      10.91B |
| 2025-12-17 |        18 |       7.20B |
| 2025-12-19 |        23 |      13.82B |
| 2025-12-21 |        20 |      14.52B |
| 2025-12-23 |        25 |      16.45B |
| 2025-12-25 |        22 |      12.54B |
| 2025-12-27 |        22 |      15.66B |
| 2025-12-29 |        22 |      17.56B |
| 2025-12-31 |        23 |      21.80B |
| 2026-01-02 |        21 |      21.05B |
| 2026-01-04 |        26 |      16.19B |
| 2026-01-06 |        19 |      12.66B |
| 2026-01-08 |        27 |      27.98B |
| 2026-01-10 |        18 |      10.61B |
| 2026-01-12 |        28 |      30.00B |
| 2026-01-14 |        29 |      28.27B |
| 2026-01-16 |        26 |      19.90B |
| 2026-01-18 |        18 |      14.61B |
| 2026-01-20 |        26 |      23.10B |
| 2026-01-22 |        23 |      22.47B |
| 2026-01-24 |        26 |      34.74B |
| 2026-01-26 |        23 |      22.59B |
| 2026-01-28 |        26 |      15.07B |
| 2026-01-30 |        22 |      14.76B |
| 2026-02-01 |        24 |      14.37B |
| 2026-02-03 |        29 |      36.18B |
| 2026-02-05 |        27 |      28.75B |
| 2026-02-07 |        25 |      30.53B |
| 2026-02-09 |        28 |      35.26B |
| 2026-02-11 |        21 |      29.65B |
| 2026-02-13 |        29 |      21.41B |
| 2026-02-15 |        21 |      24.49B |
| 2026-02-17 |        24 |      19.08B |
| 2026-02-19 |        27 |      28.28B |
| 2026-02-21 |        27 |      52.37B |
| 2026-02-23 |        26 |      38.30B |
| 2026-02-25 |        29 |      44.58B |
| 2026-02-27 |        29 |      59.08B |
| 2026-03-01 |        16 |      15.13B |
| 2026-03-03 |        22 |      20.05B |
| 2026-03-05 |        41 |      79.40B |
| 2026-03-07 |        37 |      76.59B |
| 2026-03-09 |        37 |      74.23B |
| 2026-03-11 |        33 |      50.36B |
| 2026-03-13 |        29 |      43.99B |

<!-- [[[end]]] -->

</details>

<details>
<summary>Top Players over last 7 hunts</summary>
<!-- [[[cog
from analysis import players_records, as_markdown_table
print()
print(
  as_markdown_table(
    players_records(bear=2, n_lasts=7),
    columns=["#", "Player", "Score", "# Hunts"],
    justifys=["right", "left", "right", "right"],
  )
)
]]] -->

|   # | Player          |   Score | # Hunts |
| --: | :-------------- | ------: | ------: |
|   1 | CHEN陈          |  19.01B |       7 |
|   2 | Heney           |  17.86B |       5 |
|   3 | Azrael          |  16.00B |       7 |
|   4 | Shadow          |  15.78B |       6 |
|   5 | Frinkley        |  14.55B |       3 |
|   6 | Vitvik          |  14.50B |       5 |
|   7 | Ocram           |  13.46B |       5 |
|   8 | Fear            |  13.39B |       6 |
|   9 | HuiMin          |  12.41B |       7 |
|  10 | Lest            |  11.47B |       5 |
|  11 | destro          |  11.29B |       5 |
|  12 | Brica           |  11.16B |       6 |
|  13 | Wancho          |  11.11B |       5 |
|  14 | Meow            |  10.31B |       5 |
|  15 | MOnsTruM224     |   9.96B |       6 |
|  16 | SSE             |   9.76B |       5 |
|  17 | FireGOW         |   9.04B |       6 |
|  18 | KR4V3N          |   8.84B |       6 |
|  19 | Bori            |   8.70B |       4 |
|  20 | Hawkeye         |   7.07B |       6 |
|  21 | Kenpachi        |   6.84B |       5 |
|  22 | Yanta           |   6.72B |       4 |
|  23 | 球球仔          |   6.71B |       7 |
|  24 | SP1R1T          |   6.53B |       6 |
|  25 | Brgy TIBAY      |   6.30B |       4 |
|  26 | MeowAndOnly     |   6.28B |       4 |
|  27 | The Jordinator  |   6.16B |       4 |
|  28 | scorpion        |   5.61B |       5 |
|  29 | vinfinity       |   4.93B |       3 |
|  30 | Malideiter      |   4.76B |       2 |
|  31 | Rage            |   4.66B |       3 |
|  32 | Batas           |   4.32B |       2 |
|  33 | Lord Shen       |   4.25B |       4 |
|  34 | Lady KimmyKakes |   3.81B |       2 |
|  35 | The Bob         |   3.64B |       2 |
|  36 | Shamalamaba     |   3.48B |       3 |
|  37 | TW拍吉          |   2.95B |       6 |
|  38 | 하루&까망       |   2.90B |       5 |
|  39 | Lord_DJ         |   2.86B |       3 |
|  40 | Shalamamaba     |   2.55B |       2 |
|  41 | KimmyKakes      |   2.39B |       1 |
|  42 | LordPeanut      |   2.30B |       2 |
|  43 | 帕殿咚          |   2.22B |       3 |
|  44 | vinfinitiy      |   1.69B |       1 |
|  45 | Willow          |   1.54B |       2 |
|  46 | Saint Xitar     |   1.39B |       1 |
|  47 | KittyCopia      |   1.28B |       1 |
|  48 | Queen of Hearts |   1.11B |       1 |
|  49 | 趴懶大          | 970.91M |       5 |
|  50 | Helzu           | 865.91M |       1 |
|  51 | LordGiga        | 608.25M |       2 |
|  52 | Morphose        | 434.78M |       1 |
|  53 | Ukel            | 427.65M |       1 |
|  54 | Kings Scooby    | 282.55M |       3 |
|  55 | KOREA장태욱     | 277.01M |       2 |
|  56 | CiusPorpoise    |  31.87M |       1 |
|  57 | George Floyd    |   4.46M |       1 |

<!-- [[[end]]] -->

</details>
