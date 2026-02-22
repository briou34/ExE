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

![Bear Participation](images/2026-02-22_hive_participation.png)

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

![Bear 1 damages graph](images/2026-02-22_bear1_damages.png)

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
|   1 | Paerdekop       |  13.09B |       7 |
|   2 | Shell2y         |  10.59B |       6 |
|   3 | Sjefen          |  10.54B |       6 |
|   4 | Troka           |  10.21B |       7 |
|   5 | Kenz            |  10.11B |       6 |
|   6 | JoeyBootzz      |   9.89B |       7 |
|   7 | Briou           |   9.23B |       7 |
|   8 | Coma            |   8.95B |       6 |
|   9 | Llyod Frontera  |   8.76B |       6 |
|  10 | LadyLove        |   8.69B |       6 |
|  11 | LEA             |   8.16B |       7 |
|  12 | IrotRiot        |   7.89B |       6 |
|  13 | FallingRegrets  |   7.01B |       6 |
|  14 | EmmyLou         |   6.02B |       7 |
|  15 | Lyghtz          |   5.77B |       3 |
|  16 | DarkPanda       |   5.62B |       4 |
|  17 | PapiChurro      |   5.18B |       5 |
|  18 | AZIZ            |   4.49B |       3 |
|  19 | Sir Bishop      |   4.36B |       6 |
|  20 | Cery            |   4.19B |       6 |
|  21 | Kenpachi        |   3.83B |       4 |
|  22 | MasterkinG32    |   3.61B |       4 |
|  23 | Kay_forshort    |   2.73B |       5 |
|  24 | Persian Gulf    |   2.39B |       3 |
|  25 | Lord_DJ         |   2.38B |       4 |
|  26 | DeathAmongstUs  |   2.25B |       3 |
|  27 | Lou_Scunt       |   2.22B |       3 |
|  28 | Hawkeye         |   2.06B |       4 |
|  29 | Queen of Hearts |   2.00B |       2 |
|  30 | O D I N         |   1.82B |       3 |
|  31 | scorpion        |   1.56B |       2 |
|  32 | Donald Porpoise |   1.41B |       3 |
|  33 | Shadow          |   1.39B |       1 |
|  34 | Morphose        |   1.38B |       2 |
|  35 | Tiffany         |   1.37B |       2 |
|  36 | LightsOutL      |   1.13B |       2 |
|  37 | M E D U S A     |   1.08B |       2 |
|  38 | Trillbill       |   1.03B |       2 |
|  39 | CiusPorpoise    | 957.33M |       7 |
|  40 | mary            | 905.22M |       2 |
|  41 | MOnsTruM224     | 828.01M |       1 |
|  42 | Loading         | 668.34M |       1 |
|  43 | Lord Adoniran   | 557.32M |       1 |
|  44 | KittyCopia      | 525.24M |       1 |
|  45 | SARAH           | 445.31M |       1 |
|  46 | 趴懶大          | 435.71M |       3 |
|  47 | Azrael          | 424.43M |       1 |
|  48 | 帕殿咚          | 386.78M |       1 |
|  49 | Ocram           | 382.53M |       1 |
|  50 | Pain            | 346.73M |       1 |
|  51 | Ukel            | 204.29M |       1 |
|  52 | Trimute         | 148.32M |       1 |
|  53 | George Floyd    |  64.52M |       2 |

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

![Bear 2 damages graph](images/2026-02-22_bear2_damages.png)

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
|   1 | Frinkley        |  13.88B |       5 |
|   2 | CHEN陈          |  13.86B |       6 |
|   3 | Fear            |  12.53B |       7 |
|   4 | Ocram           |  11.35B |       5 |
|   5 | Brica           |  10.70B |       7 |
|   6 | Azrael          |   9.80B |       6 |
|   7 | Shadow          |   9.51B |       6 |
|   8 | HuiMin          |   9.45B |       7 |
|   9 | 球球仔          |   8.83B |       7 |
|  10 | vinfinity       |   8.06B |       5 |
|  11 | Rage            |   8.01B |       5 |
|  12 | KR4V3N          |   7.20B |       5 |
|  13 | SP1R1T          |   6.99B |       7 |
|  14 | Bori            |   6.64B |       5 |
|  15 | FireGOW         |   6.18B |       5 |
|  16 | Loading         |   6.14B |       6 |
|  17 | Sked            |   5.66B |       5 |
|  18 | KittyCopia      |   5.64B |       6 |
|  19 | scorpion        |   5.16B |       5 |
|  20 | AZIZ            |   5.05B |       3 |
|  21 | MOnsTruM224     |   4.72B |       5 |
|  22 | 帕殿咚          |   4.65B |       6 |
|  23 | 하루&까망       |   3.32B |       7 |
|  24 | Persian Gulf    |   3.11B |       3 |
|  25 | Lord_DJ         |   2.98B |       3 |
|  26 | Llyod Frontera  |   2.71B |       1 |
|  27 | Hawkeye         |   2.35B |       2 |
|  28 | Sjefen          |   2.30B |       1 |
|  29 | Cery            |   2.10B |       1 |
|  30 | The Bob         |   1.86B |       2 |
|  31 | CHEN            |   1.64B |       1 |
|  32 | TW拍吉          |   1.29B |       7 |
|  33 | LordGiga        |   1.11B |       3 |
|  34 | Queen of Hearts |   1.06B |       1 |
|  35 | KOREA장태욱     | 820.19M |       4 |
|  36 | Ukel            | 782.99M |       4 |
|  37 | 趴懶大          | 744.62M |       4 |
|  38 | Willow          | 665.93M |       1 |
|  39 | 熾星空          | 568.14M |       1 |
|  40 | Kings Scooby    | 433.70M |       1 |
|  41 | Trimute         | 261.74M |       1 |
|  42 | HASANNEMREE     | 189.58M |       1 |
|  43 | tamere          | 181.59M |       1 |
|  44 | George Floyd    |  50.38M |       3 |

<!-- [[[end]]] -->

</details>
