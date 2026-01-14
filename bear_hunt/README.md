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

![Bear Participation](images/2026-01-14_hive_participation.png)

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

![Bear 1 damages graph](images/2026-01-14_bear1_damages.png)

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
|   1 | Coma             |   7.74B |       6 |
|   2 | Lyghtz           |   7.47B |       6 |
|   3 | Llyod Frontera   |   7.39B |       7 |
|   4 | Troka            |   6.68B |       6 |
|   5 | LadyLove         |   6.34B |       6 |
|   6 | Briou            |   5.62B |       6 |
|   7 | Cery             |   5.46B |       5 |
|   8 | FallingRegrets   |   4.87B |       5 |
|   9 | Shell2y          |   4.62B |       5 |
|  10 | DarkPanda        |   4.47B |       7 |
|  11 | BadCiuSpencer    |   4.19B |       6 |
|  12 | LEA              |   3.93B |       7 |
|  13 | Darth Porpoise   |   3.48B |       6 |
|  14 | Ocram            |   3.44B |       2 |
|  15 | Paerdekop        |   3.33B |       2 |
|  16 | IrotRiot         |   3.33B |       5 |
|  17 | Sir Bishop       |   2.91B |       7 |
|  18 | Kenz             |   2.86B |       3 |
|  19 | Kenpachi         |   2.24B |       3 |
|  20 | Señor Bootie     |   2.20B |       3 |
|  21 | EmmyLou          |   2.00B |       3 |
|  22 | M E D U S A      |   1.97B |       3 |
|  23 | Lord_DJ          |   1.92B |       4 |
|  24 | Queen of Hearts  |   1.87B |       3 |
|  25 | mary             |   1.63B |       4 |
|  26 | Shadow           |   1.42B |       2 |
|  27 | Trillbill        |   1.42B |       3 |
|  28 | scorpion         |   1.35B |       4 |
|  29 | Kay_forshort     |   1.25B |       3 |
|  30 | PapiChurro       |   1.23B |       3 |
|  31 | Sjefen           |   1.20B |       1 |
|  32 | TheGlizzinator   |   1.11B |       2 |
|  33 | AZIZ             |   1.10B |       1 |
|  34 | MasterkinG32     | 794.07M |       2 |
|  35 | 帕殿咚           | 744.35M |       1 |
|  36 | DeathAmongstUs   | 721.20M |       2 |
|  37 | Morphose         | 564.59M |       2 |
|  38 | Azrael           | 481.44M |       1 |
|  39 | Hawkeye          | 457.65M |       2 |
|  40 | MOnsTruM224      | 448.48M |       1 |
|  41 | yacob            | 414.01M |       3 |
|  42 | Lord Adoniran    | 337.91M |       2 |
|  43 | Persian Gulf     | 335.71M |       1 |
|  44 | Tiffany          | 326.53M |       1 |
|  45 | O D I N          | 319.26M |       1 |
|  46 | Supernova        | 310.92M |       2 |
|  47 | MOnSTruM224      | 273.41M |       1 |
|  48 | Lady Emily       | 261.85M |       2 |
|  49 | Cavendish        | 238.36M |       1 |
|  50 | StepMothers Milk | 222.71M |       1 |
|  51 | ROSTR            | 153.07M |       1 |
|  52 | 趴懶大           |  81.70M |       1 |
|  53 | BelalShash       |  47.41M |       1 |
|  54 | BlackBebe        |  20.25M |       1 |

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

![Bear 2 damages graph](images/2026-01-14_bear2_damages.png)

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
|   1 | CHEN陈           |  12.10B |       7 |
|   2 | Ocram            |   9.91B |       5 |
|   3 | HuiMin           |   7.78B |       7 |
|   4 | AZIZ             |   7.34B |       6 |
|   5 | SP1R1T           |   6.98B |       7 |
|   6 | 球球仔           |   6.45B |       7 |
|   7 | Brica            |   5.96B |       7 |
|   8 | Azrael           |   5.87B |       5 |
|   9 | Sjefen           |   5.85B |       5 |
|  10 | Frinkley         |   5.73B |       3 |
|  11 | Shadow           |   5.62B |       5 |
|  12 | Bori             |   5.46B |       5 |
|  13 | Fear             |   5.42B |       5 |
|  14 | 帕殿咚           |   5.36B |       6 |
|  15 | TW拍吉           |   4.32B |       6 |
|  16 | KR4VEN           |   3.99B |       3 |
|  17 | Rage             |   3.83B |       4 |
|  18 | Kai              |   2.85B |       2 |
|  19 | momo&하루        |   2.66B |       7 |
|  20 | Persian Gulf     |   2.38B |       4 |
|  21 | scorpion         |   2.11B |       3 |
|  22 | Lord_DJ          |   1.97B |       3 |
|  23 | Sked             |   1.89B |       3 |
|  24 | AussieJosh       |   1.63B |       1 |
|  25 | Hawkeye          |   1.56B |       2 |
|  26 | The Bob          |   1.46B |       2 |
|  27 | vinfinity        |   1.45B |       2 |
|  28 | Queen of Hearts  |   1.39B |       1 |
|  29 | Cery             |   1.37B |       1 |
|  30 | Ppap             |   1.09B |       2 |
|  31 | 趴懶大           | 869.75M |       4 |
|  32 | Kay_forshort     | 834.99M |       1 |
|  33 | MasterkinG32     | 831.17M |       1 |
|  34 | Loading          | 789.53M |       1 |
|  35 | Trimute          | 720.55M |       3 |
|  36 | tamere           | 684.72M |       2 |
|  37 | GodOfWhores      | 641.13M |       1 |
|  38 | 차은아           | 616.55M |       2 |
|  39 | Doon             | 565.38M |       1 |
|  40 | The KING TUT     | 322.20M |       2 |
|  41 | Ukel             | 311.76M |       2 |
|  42 | KOREA장태욱      | 281.76M |       3 |
|  43 | yacob            | 245.41M |       2 |
|  44 | LordGiga         | 201.98M |       2 |
|  45 | XLR8R            | 196.05M |       1 |
|  46 | HASANNEMREE      | 116.77M |       1 |
|  47 | HASANN EMREE     |  87.57M |       1 |
|  48 | Lord Keith       |  58.87M |       1 |
|  49 | ROSTR            |  54.22M |       1 |
|  50 | Mazzoni          |  51.90M |       1 |
|  51 | Supernova        |  45.67M |       1 |
|  52 | maxee            |   4.35M |       1 |
|  53 | I am your father |   3.69M |       1 |

<!-- [[[end]]] -->

</details>
