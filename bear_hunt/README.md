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

![Bear Participation](images/2025-12-03_hive_participation.png)

<!-- [[[end]]] -->

<!-- [[[cog
# Display the future hive participation map once cities start moving
import re
from pathlib import Path
import yaml

MOVING = yaml.safe_load(Path("hive", "locations_moving.yml").open("r"))
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

![Bear Participation](images/2025-12-03_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2025-12-03_bear1_damages.png)

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
|   1 | Cery             |   7.09B |       7 |
|   2 | Lyghtz           |   6.11B |       6 |
|   3 | Coma             |   5.38B |       6 |
|   4 | 達努巴克         |   4.69B |       5 |
|   5 | Briou            |   4.38B |       7 |
|   6 | Troka            |   3.72B |       7 |
|   7 | LadyLove         |   3.39B |       6 |
|   8 | IrotRiot         |   3.38B |       5 |
|   9 | Llyod Frontera   |   3.33B |       5 |
|  10 | Sjefen           |   3.23B |       5 |
|  11 | CiusconUnchained |   3.22B |       6 |
|  12 | Azrael           |   3.22B |       6 |
|  13 | FallingRegrets   |   2.95B |       6 |
|  14 | Lord_DJ          |   2.16B |       6 |
|  15 | LEA              |   2.09B |       7 |
|  16 | Queen of Hearts  |   1.82B |       4 |
|  17 | DarkPanda        |   1.80B |       6 |
|  18 | Lllyod Frontera  |   1.38B |       2 |
|  19 | Sir Bishop       |   1.31B |       7 |
|  20 | Aziz             |   1.30B |       2 |
|  21 | Shellybobs       |   1.10B |       2 |
|  22 | Ocram            | 968.51M |       1 |
|  23 | BlackBebe        | 807.13M |       2 |
|  24 | Lord Adoniran    | 741.33M |       3 |
|  25 | Darth Porpoise   | 689.49M |       3 |
|  26 | Queen of Cats    | 617.09M |       2 |
|  27 | Brica            | 435.64M |       1 |
|  28 | MOnsTrUM224      | 369.26M |       2 |
|  29 | Kenpachi         | 324.52M |       1 |
|  30 | 趴懶大           | 289.50M |       2 |
|  31 | Dumblidore       | 231.74M |       1 |
|  32 | Morphose         | 199.41M |       1 |
|  33 | scorpion         | 170.06M |       1 |
|  34 | Supernova        | 152.98M |       2 |
|  35 | Kay_forshort     | 115.21M |       1 |
|  36 | HasannEmree      |  97.92M |       1 |
|  37 | Trimute          |  82.57M |       1 |
|  38 | ROSTR            |  48.95M |       3 |
|  39 | Nubian King 13   |  39.41M |       1 |
|  40 | 차은아           |  21.18M |       1 |

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

![Bear 2 damages graph](images/2025-12-03_bear2_damages.png)

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
|   1 | CHEN陈           |   9.35B |       7 |
|   2 | Ocram            |   6.21B |       6 |
|   3 | Frinkley         |   5.81B |       4 |
|   4 | TW拍吉           |   5.79B |       7 |
|   5 | Aziz             |   4.82B |       5 |
|   6 | brfc             |   4.15B |       6 |
|   7 | HuiMin           |   4.07B |       7 |
|   8 | 球球仔           |   3.13B |       7 |
|   9 | DoRaeMi          |   3.10B |       5 |
|  10 | Brett Sinclair   |   3.01B |       4 |
|  11 | Brica            |   2.99B |       6 |
|  12 | Fear             |   2.97B |       5 |
|  13 | Professor        |   2.77B |       4 |
|  14 | Rage             |   2.64B |       5 |
|  15 | 屁屁俠           |   2.29B |       6 |
|  16 | 少量課金者       |   2.19B |       5 |
|  17 | SP1R1T           |   1.99B |       4 |
|  18 | Sked             |   1.89B |       6 |
|  19 | Scorpion         |   1.55B |       2 |
|  20 | Shakieee         |   1.21B |       2 |
|  21 | 趴懶大           |   1.18B |       5 |
|  22 | scorpion         | 885.90M |       2 |
|  23 | Nubian King 13   | 535.12M |       4 |
|  24 | Kenpachi         | 522.41M |       2 |
|  25 | Azrael           | 491.33M |       1 |
|  26 | Lord_DJ          | 471.28M |       1 |
|  27 | 차은아           | 465.55M |       5 |
|  28 | tamere           | 434.80M |       1 |
|  29 | ROSTR            | 376.28M |       1 |
|  30 | Ukel             | 359.07M |       3 |
|  31 | Trimute          | 215.87M |       2 |
|  32 | Shell            | 191.35M |       2 |
|  33 | Saiint           | 184.71M |       1 |
|  34 | Queen of Hearts  | 176.24M |       1 |
|  35 | Supernova        | 144.43M |       2 |
|  36 | LordGiga         | 115.55M |       2 |
|  37 | Doon             | 113.71M |       1 |
|  38 | The KING TUTEvil | 112.93M |       1 |
|  39 | Morphose         |  87.11M |       1 |
|  40 | King Koopa       |  82.05M |       1 |
|  41 | ĎiäbLo           |  73.10M |       1 |
|  42 | 熾星空           |  30.90M |       2 |
|  43 | The KING TUT     |  26.03M |       1 |
|  44 | Lord Adoniran    |  21.39M |       1 |
|  45 | 是17呀           |  17.06M |       1 |
|  46 | Sjefen           |  13.85M |       1 |
|  47 | Lord Keith       |  11.59M |       1 |

<!-- [[[end]]] -->

</details>
