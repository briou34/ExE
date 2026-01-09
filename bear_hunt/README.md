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

![Bear Participation](images/2026-01-09_hive_participation.png)

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

![Bear 1 damages graph](images/2026-01-09_bear1_damages.png)

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

|   # | Player           |   Score | # Hunts |
| --: | :--------------- | ------: | ------: |
|   1 | Lyghtz           |   8.39B |       7 |
|   2 | Coma             |   8.03B |       6 |
|   3 | Llyod Frontera   |   7.59B |       7 |
|   4 | Troka            |   6.70B |       6 |
|   5 | Cery             |   6.63B |       5 |
|   6 | LadyLove         |   6.28B |       6 |
|   7 | Briou            |   5.78B |       6 |
|   8 | Ocram            |   5.11B |       3 |
|   9 | IrotRiot         |   5.03B |       5 |
|  10 | BadCiuSpencer    |   4.90B |       6 |
|  11 | FallingRegrets   |   4.45B |       5 |
|  12 | Shell2y          |   4.43B |       4 |
|  13 | DarkPanda        |   3.87B |       7 |
|  14 | LEA              |   3.56B |       7 |
|  15 | Darth Porpoise   |   3.43B |       6 |
|  16 | Sir Bishop       |   2.77B |       7 |
|  17 | AZIZ             |   2.42B |       2 |
|  18 | Lord_DJ          |   2.32B |       5 |
|  19 | The Bob          |   1.80B |       2 |
|  20 | Queen of Hearts  |   1.71B |       3 |
|  21 | Mill2y           |   1.57B |       1 |
|  22 | 達努巴克         |   1.55B |       1 |
|  23 | Kenpachi         |   1.50B |       2 |
|  24 | Kay_forshort     |   1.45B |       4 |
|  25 | Shadow           |   1.30B |       1 |
|  26 | Trillbill        |   1.22B |       4 |
|  27 | mary             |   1.19B |       3 |
|  28 | scorpion         |   1.18B |       3 |
|  29 | MasterkinG32     | 794.07M |       2 |
|  30 | Senor Bootie     | 747.97M |       1 |
|  31 | EmmyLou          | 584.93M |       1 |
|  32 | Kenz             | 579.71M |       1 |
|  33 | M E D U S A      | 541.73M |       1 |
|  34 | Morphose         | 534.70M |       1 |
|  35 | Sked             | 523.71M |       1 |
|  36 | Azrael           | 481.44M |       1 |
|  37 | Supernova        | 400.65M |       3 |
|  38 | DeathAmongstUs   | 346.24M |       1 |
|  39 | Lord Adoniran    | 337.91M |       2 |
|  40 | Persian Gulf     | 335.71M |       1 |
|  41 | MOnSTruM224      | 273.41M |       1 |
|  42 | Lady Emily       | 261.85M |       2 |
|  43 | Cavendish        | 238.36M |       1 |
|  44 | PapiChurro       | 236.37M |       1 |
|  45 | StepMothers Milk | 222.71M |       1 |
|  46 | 趴懶大           | 220.48M |       3 |
|  47 | The KING TUT     | 200.99M |       2 |
|  48 | ROSTR            | 153.07M |       1 |
|  49 | Hawkeye          | 107.35M |       1 |
|  50 | yacob            |  80.81M |       1 |
|  51 | Thadeus          |  50.89M |       1 |
|  52 | BelalShash       |  47.41M |       1 |
|  53 | King of Dogs     |  38.30M |       1 |
|  54 | Trimute          |  36.51M |       1 |
|  55 | XLR8R            |  27.03M |       1 |
|  56 | BlackBebe        |  20.25M |       1 |
|  57 | Fear             |   7.92M |       1 |
|  58 | maxee            |   6.59M |       1 |

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

![Bear 2 damages graph](images/2026-01-09_bear2_damages.png)

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
|   1 | CHEN陈           |  12.85B |       7 |
|   2 | HuiMin           |   8.08B |       7 |
|   3 | Ocram            |   7.70B |       4 |
|   4 | Shadow           |   7.25B |       6 |
|   5 | Frinkley         |   7.17B |       4 |
|   6 | SP1R1T           |   6.42B |       7 |
|   7 | Sjefen           |   6.19B |       6 |
|   8 | 球球仔           |   5.85B |       7 |
|   9 | Bori             |   5.75B |       5 |
|  10 | 帕殿咚           |   5.70B |       7 |
|  11 | Azrael           |   5.47B |       5 |
|  12 | AZIZ             |   5.38B |       5 |
|  13 | Brica            |   5.31B |       6 |
|  14 | Rage             |   4.41B |       5 |
|  15 | TW拍吉           |   4.10B |       6 |
|  16 | Fear             |   3.62B |       4 |
|  17 | Kai              |   2.85B |       2 |
|  18 | Persian Gulf     |   2.81B |       6 |
|  19 | scorpion         |   2.67B |       4 |
|  20 | momo&하루        |   2.37B |       6 |
|  21 | Hawkeye          |   2.00B |       3 |
|  22 | KR4VEN           |   1.50B |       1 |
|  23 | Lord_DJ          |   1.49B |       2 |
|  24 | The Bob          |   1.46B |       2 |
|  25 | Queen of Hearts  |   1.39B |       1 |
|  26 | Cery             |   1.37B |       1 |
|  27 | Sked             |   1.21B |       2 |
|  28 | MasterkinG32     |   1.19B |       2 |
|  29 | Ppap             |   1.09B |       2 |
|  30 | Professor        |   1.07B |       1 |
|  31 | Kay_forshort     | 834.99M |       1 |
|  32 | GodOfWhores      | 641.13M |       1 |
|  33 | 趴懶大           | 581.30M |       3 |
|  34 | Doon             | 565.38M |       1 |
|  35 | vinfinity        | 553.93M |       1 |
|  36 | Trimute          | 545.30M |       2 |
|  37 | tamere           | 487.67M |       1 |
|  38 | yacob            | 476.16M |       3 |
|  39 | 차은아           | 457.04M |       2 |
|  40 | The KING TUT     | 322.20M |       2 |
|  41 | Ukel             | 311.76M |       2 |
|  42 | Kjs722           | 243.91M |       1 |
|  43 | LordGiga         | 201.98M |       2 |
|  44 | KOREA장태욱      | 198.41M |       2 |
|  45 | XLR8R            | 196.05M |       1 |
|  46 | HasannEmree      | 148.95M |       2 |
|  47 | HASANNEMREE      | 116.77M |       1 |
|  48 | ROSTR            | 116.33M |       1 |
|  49 | Nubian King 13   |  72.60M |       1 |
|  50 | Lord Keith       |  58.87M |       1 |
|  51 | Mazzoni          |  51.90M |       1 |
|  52 | maxee            |   4.35M |       1 |
|  53 | I am your father |   3.69M |       1 |

<!-- [[[end]]] -->

</details>
