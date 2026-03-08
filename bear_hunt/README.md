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

![Bear Participation](images/2026-03-08_hive_participation.png)

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

![Bear Participation](images/2026-03-08_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2026-03-08_bear1_damages.png)

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
|   1 | Coma            |  15.93B |       7 |
|   2 | Sjefen          |  15.40B |       7 |
|   3 | Paerdekop       |  14.96B |       6 |
|   4 | Lyghtz          |  14.51B |       7 |
|   5 | Llyod Frontera  |  14.13B |       7 |
|   6 | Kenz            |  13.92B |       7 |
|   7 | JoeyBootzz      |  12.91B |       7 |
|   8 | Shell2y         |  12.61B |       6 |
|   9 | LadyLove        |  12.55B |       7 |
|  10 | AZIZ            |  12.39B |       7 |
|  11 | Briou           |  11.93B |       7 |
|  12 | DarkPanda       |  10.41B |       7 |
|  13 | Cery            |  10.05B |       6 |
|  14 | Troka           |   9.79B |       6 |
|  15 | FallingRegrets  |   9.56B |       6 |
|  16 | LEA             |   8.86B |       6 |
|  17 | PapiChurro      |   7.05B |       5 |
|  18 | Sir Bishop      |   6.00B |       7 |
|  19 | IrotRiot        |   5.28B |       5 |
|  20 | EmmyLou         |   5.17B |       5 |
|  21 | Kay_forshort    |   4.86B |       7 |
|  22 | Lord Adoniran   |   3.80B |       4 |
|  23 | DeathAmongstUs  |   3.50B |       4 |
|  24 | KESHKERES       |   3.43B |       2 |
|  25 | Ocram           |   3.38B |       2 |
|  26 | Frinkley        |   2.96B |       1 |
|  27 | Kenpachi        |   2.27B |       2 |
|  28 | mary            |   2.14B |       3 |
|  29 | Donald Porpoise |   1.89B |       5 |
|  30 | Saint Xitar     |   1.79B |       1 |
|  31 | Ellie Softpaw   |   1.79B |       2 |
|  32 | 帕殿咚          |   1.64B |       3 |
|  33 | LightsOutL      |   1.54B |       3 |
|  34 | Shadow          |   1.53B |       1 |
|  35 | MasterkinG32    |   1.52B |       2 |
|  36 | Brica           |   1.46B |       1 |
|  37 | CravenMoorehead |   1.31B |       2 |
|  38 | Queen of Hearts |   1.25B |       3 |
|  39 | Lagertha        |   1.16B |       1 |
|  40 | ODIN            | 951.66M |       1 |
|  41 | Lord_DJ         | 946.90M |       1 |
|  42 | O D I N         | 944.83M |       2 |
|  43 | M E D U S A     | 864.95M |       1 |
|  44 | Loading         | 856.10M |       1 |
|  45 | MOnsTruM224     | 849.71M |       1 |
|  46 | Helzu           | 825.96M |       1 |
|  47 | CiusPorpoise    | 758.80M |       3 |
|  48 | Trillbill       | 702.26M |       1 |
|  49 | Diablo          | 294.47M |       2 |
|  50 | Cavendish       | 273.10M |       1 |
|  51 | LordGiga        | 260.10M |       2 |
|  52 | yacob           | 254.48M |       1 |
|  53 | SARAH           | 235.66M |       1 |
|  54 | Ukel            | 228.60M |       1 |
|  55 | King Koopa      | 209.50M |       2 |
|  56 | 趴懶大          |  92.24M |       1 |
|  57 | George Floyd    |  25.67M |       3 |

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

![Bear 2 damages graph](images/2026-03-08_bear2_damages.png)

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

|   # | Player           |   Score | # Hunts |
| --: | :--------------- | ------: | ------: |
|   1 | Frinkley         |  23.50B |       5 |
|   2 | CHEN陈           |  21.01B |       7 |
|   3 | Azrael           |  16.33B |       7 |
|   4 | Shadow           |  15.99B |       6 |
|   5 | HuiMin           |  15.10B |       7 |
|   6 | Ocram            |  15.05B |       5 |
|   7 | Fear             |  14.78B |       6 |
|   8 | Brica            |  12.38B |       6 |
|   9 | Rage             |  10.79B |       5 |
|  10 | KR4V3N           |  10.16B |       7 |
|  11 | Bori             |   9.78B |       5 |
|  12 | scorpion         |   9.67B |       7 |
|  13 | SP1R1T           |   8.91B |       6 |
|  14 | FireGOW          |   8.79B |       6 |
|  15 | 球球仔           |   8.49B |       7 |
|  16 | Heney            |   7.11B |       2 |
|  17 | MOnsTruM224      |   6.79B |       4 |
|  18 | Vitvik           |   6.75B |       2 |
|  19 | Hawkeye          |   6.12B |       5 |
|  20 | Persian Gulf     |   5.47B |       3 |
|  21 | vinfinity        |   5.42B |       2 |
|  22 | Wancho           |   5.19B |       2 |
|  23 | Meow             |   5.14B |       2 |
|  24 | destro           |   4.97B |       2 |
|  25 | KittyCopia       |   4.89B |       4 |
|  26 | Lest             |   4.65B |       2 |
|  27 | Batas            |   4.32B |       2 |
|  28 | MeowsDaddy       |   4.11B |       2 |
|  29 | Lord_DJ          |   4.11B |       4 |
|  30 | SSE              |   3.97B |       2 |
|  31 | Lady KimmyKakes  |   3.81B |       2 |
|  32 | Yanta            |   3.61B |       2 |
|  33 | Paerdekop        |   3.26B |       1 |
|  34 | Kenpachi         |   3.17B |       2 |
|  35 | The Bob          |   3.07B |       2 |
|  36 | Malideiter       |   2.94B |       1 |
|  37 | TW拍吉           |   2.89B |       5 |
|  38 | 하루&까망        |   2.81B |       5 |
|  39 | Brgy TIBAY       |   2.77B |       2 |
|  40 | Loading          |   2.48B |       2 |
|  41 | LordPeanut       |   2.30B |       2 |
|  42 | 帕殿咚           |   2.15B |       3 |
|  43 | vinfinitiy       |   1.69B |       1 |
|  44 | Sked             |   1.59B |       2 |
|  45 | The Jordinator   |   1.58B |       1 |
|  46 | Willow           |   1.54B |       2 |
|  47 | Lord Shen        |   1.45B |       1 |
|  48 | Saint Xitar      |   1.39B |       1 |
|  49 | MasterkinG32     |   1.26B |       1 |
|  50 | Shamalamaba      | 967.08M |       1 |
|  51 | Ukel             | 925.17M |       3 |
|  52 | Shalamamaba      | 907.80M |       1 |
|  53 | Helzu            | 865.91M |       1 |
|  54 | 趴懶大           | 809.11M |       4 |
|  55 | tamere           | 742.69M |       1 |
|  56 | Trimute          | 683.35M |       3 |
|  57 | Kings Scooby     | 479.87M |       3 |
|  58 | KOREA장태욱      | 443.13M |       4 |
|  59 | Morphose         | 434.78M |       1 |
|  60 | HASANNEMREE      | 212.77M |       1 |
|  61 | 熾星空           | 115.19M |       1 |
|  62 | CiusPorpoise     |  31.87M |       1 |
|  63 | George Floyd     |  27.54M |       4 |
|  64 | I am your father |   2.45M |       1 |

<!-- [[[end]]] -->

</details>
