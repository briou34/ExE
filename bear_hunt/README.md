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

![Bear Participation](images/2026-02-11_hive_participation.png)

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

![Bear Participation](images/2026-02-11_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2026-02-11_bear1_damages.png)

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
|   1 | Sjefen          |  12.57B |       7 |
|   2 | Paerdekop       |  12.37B |       6 |
|   3 | Llyod Frontera  |  11.91B |       7 |
|   4 | Shell2y         |  11.51B |       7 |
|   5 | JoeyBootzz      |  10.26B |       7 |
|   6 | LadyLove        |  10.20B |       7 |
|   7 | Briou           |  10.11B |       7 |
|   8 | Kenz            |   9.72B |       6 |
|   9 | Troka           |   9.39B |       6 |
|  10 | IrotRiot        |   8.97B |       6 |
|  11 | PapiChurro      |   7.74B |       6 |
|  12 | FallingRegrets  |   7.21B |       7 |
|  13 | LEA             |   6.82B |       6 |
|  14 | Coma            |   6.79B |       5 |
|  15 | Cery            |   6.76B |       6 |
|  16 | EmmyLou         |   6.45B |       7 |
|  17 | DarkPanda       |   5.29B |       5 |
|  18 | Ocram           |   5.07B |       3 |
|  19 | Lyghtz          |   4.81B |       3 |
|  20 | Hugh_Janus      |   4.34B |       6 |
|  21 | Sir Bishop      |   3.86B |       7 |
|  22 | M E D U S A     |   3.46B |       4 |
|  23 | Queen of Hearts |   3.40B |       4 |
|  24 | MasterkinG32    |   3.29B |       4 |
|  25 | Lord_DJ         |   3.07B |       5 |
|  26 | DeathAmongstUs  |   2.78B |       4 |
|  27 | Kenpachi        |   2.21B |       2 |
|  28 | Kay_forshort    |   2.20B |       4 |
|  29 | Shadow          |   1.91B |       2 |
|  30 | O D I N         |   1.87B |       3 |
|  31 | Trillbill       |   1.72B |       3 |
|  32 | MOnsTruM224     |   1.68B |       4 |
|  33 | scorpion        |   1.68B |       2 |
|  34 | Tiffany         |   1.22B |       2 |
|  35 | Pain            |   1.15B |       3 |
|  36 | LightsOutL      |   1.06B |       2 |
|  37 | Donald Porpoise |   1.02B |       2 |
|  38 | CiusPorpoise    | 984.36M |       5 |
|  39 | mary            | 905.22M |       2 |
|  40 | Diablo          | 803.91M |       2 |
|  41 | yacob           | 782.09M |       3 |
|  42 | Hawkeye         | 776.19M |       2 |
|  43 | Dunndertaker    | 755.95M |       2 |
|  44 | 帕殿咚          | 714.23M |       1 |
|  45 | Loading         | 668.34M |       1 |
|  46 | AZIZ            | 537.72M |       1 |
|  47 | SP1R1T          | 427.84M |       1 |
|  48 | Azrael          | 424.43M |       1 |
|  49 | Cavendish       | 353.92M |       1 |
|  50 | KittyCopia      | 341.07M |       1 |
|  51 | Trimute         | 244.34M |       1 |
|  52 | Thadeus         | 223.49M |       2 |
|  53 | 趴懶大          | 206.37M |       2 |
|  54 | Cloney Jr       | 144.56M |       1 |
|  55 | George Floyd    |  35.18M |       1 |

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

![Bear 2 damages graph](images/2026-02-11_bear2_damages.png)

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
|   1 | CHEN陈          |  15.19B |       7 |
|   2 | Frinkley        |  12.97B |       5 |
|   3 | Fear            |  10.47B |       6 |
|   4 | Brica           |   9.32B |       7 |
|   5 | 球球仔          |   9.02B |       7 |
|   6 | HuiMin          |   8.97B |       7 |
|   7 | Azrael          |   8.95B |       6 |
|   8 | Ocram           |   8.40B |       4 |
|   9 | Shadow          |   7.70B |       5 |
|  10 | AZIZ            |   7.23B |       5 |
|  11 | SP1R1T          |   6.93B |       6 |
|  12 | Rage            |   6.89B |       5 |
|  13 | vinfinity       |   6.12B |       4 |
|  14 | Loading         |   6.11B |       6 |
|  15 | 帕殿咚          |   5.82B |       6 |
|  16 | Persian Gulf    |   5.32B |       6 |
|  17 | FireGOW         |   5.24B |       4 |
|  18 | KittyCopia      |   5.12B |       6 |
|  19 | Hawkeye         |   4.88B |       5 |
|  20 | KR4V3N          |   4.13B |       3 |
|  21 | Sked            |   4.11B |       5 |
|  22 | scorpion        |   4.10B |       4 |
|  23 | The Bob         |   3.79B |       3 |
|  24 | 하루&까망       |   3.52B |       7 |
|  25 | MOnsTruM224     |   2.21B |       2 |
|  26 | Lyghtz          |   2.21B |       1 |
|  27 | Lord_DJ         |   1.99B |       2 |
|  28 | Bori            |   1.89B |       3 |
|  29 | TW拍吉          |   1.40B |       7 |
|  30 | LordGiga        |   1.17B |       3 |
|  31 | DarkPanda       |   1.08B |       1 |
|  32 | Queen of Hearts |   1.06B |       1 |
|  33 | AussieJosh      |   1.00B |       1 |
|  34 | Ukel            | 998.13M |       3 |
|  35 | Trimute         | 948.39M |       3 |
|  36 | tamere          | 928.47M |       1 |
|  37 | 趴懶大          | 885.75M |       4 |
|  38 | KOREA장태욱     | 587.46M |       4 |
|  39 | Kings Scooby    | 555.56M |       4 |
|  40 | ROSTR           | 192.59M |       2 |
|  41 | George Floyd    |  31.57M |       4 |
|  42 | 熾星空          |  22.85M |       1 |

<!-- [[[end]]] -->

</details>
