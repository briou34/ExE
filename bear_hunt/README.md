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

![Bear Participation](images/2025-12-17_hive_participation.png)

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

![Bear Participation](images/2025-12-17_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2025-12-17_bear1_damages.png)

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
|   1 | Cery             |   5.98B |       6 |
|   2 | Sjefen           |   5.39B |       6 |
|   3 | Llyod Frontera   |   5.31B |       7 |
|   4 | Lyghtz           |   4.89B |       5 |
|   5 | Troka            |   4.76B |       6 |
|   6 | Briou            |   4.54B |       7 |
|   7 | Coma             |   4.46B |       5 |
|   8 | FallingRegrets   |   4.15B |       7 |
|   9 | 達努巴克         |   4.08B |       3 |
|  10 | LadyLove         |   3.72B |       6 |
|  11 | Azrael           |   3.00B |       6 |
|  12 | Ocram            |   2.99B |       2 |
|  13 | IrotRiot         |   2.89B |       4 |
|  14 | Darth Porpoise   |   2.69B |       5 |
|  15 | Queen of Hearts  |   2.37B |       7 |
|  16 | LEA              |   2.13B |       7 |
|  17 | Lord_DJ          |   1.95B |       5 |
|  18 | DarkPanda        |   1.72B |       5 |
|  19 | Sir Bishop       |   1.37B |       7 |
|  20 | CiusconUnchained |   1.27B |       5 |
|  21 | 趴懶大           |   1.12B |       5 |
|  22 | Aziz             | 872.93M |       1 |
|  23 | Queen of Cats    | 827.18M |       2 |
|  24 | Lord Adoniran    | 714.81M |       2 |
|  25 | BlackBebe        | 670.94M |       3 |
|  26 | Kay_forshort     | 637.59M |       3 |
|  27 | Professor        | 560.21M |       1 |
|  28 | Shellybobs       | 512.78M |       1 |
|  29 | Brica            | 417.05M |       1 |
|  30 | MOnsTruM224      | 342.63M |       2 |
|  31 | Cloney Jr        | 336.21M |       2 |
|  32 | Supernova        | 301.91M |       2 |
|  33 | XLR8R            | 288.90M |       1 |
|  34 | Kenpachi         | 284.01M |       1 |
|  35 | tamere           | 279.80M |       1 |
|  36 | Dumblidore       | 206.61M |       1 |
|  37 | scorpion         | 132.54M |       1 |
|  38 | Trimute          |  99.30M |       1 |
|  39 | HasannEmree      |  97.92M |       1 |
|  40 | The KING TUT     |  77.08M |       1 |
|  41 | ROSTR            |  29.01M |       1 |
|  42 | Mazzoni          |  26.81M |       1 |
|  43 | Nubian King 13   |  25.27M |       1 |

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

![Bear 2 damages graph](images/2025-12-17_bear2_damages.png)

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

|   # | Player       |   Score | # Hunts |
| --: | :----------- | ------: | ------: |
|   1 | CHEN陈       |   9.18B |       7 |
|   2 | Ocram        |   6.58B |       5 |
|   3 | Frinkley     |   6.47B |       4 |
|   4 | TW拍吉       |   6.03B |       7 |
|   5 | 球球仔       |   5.83B |       7 |
|   6 | AZIZ         |   5.45B |       5 |
|   7 | HuiMin       |   5.42B |       7 |
|   8 | Fear         |   5.09B |       6 |
|   9 | Brica        |   4.30B |       6 |
|  10 | Rage         |   4.19B |       6 |
|  11 | SP1R1T       |   3.95B |       6 |
|  12 | 屁屁俠       |   3.61B |       6 |
|  13 | DoRaeMi      |   3.27B |       4 |
|  14 | 少量課金者   |   2.92B |       5 |
|  15 | Shakieee     |   2.54B |       6 |
|  16 | Sked         |   2.45B |       6 |
|  17 | scorpion     |   1.52B |       5 |
|  18 | Aziz         |   1.42B |       1 |
|  19 | Lord_DJ      |   1.41B |       2 |
|  20 | DoraeMi      |   1.10B |       1 |
|  21 | Professor    | 952.10M |       2 |
|  22 | Kenpachi     | 900.32M |       2 |
|  23 | Cloney Jr    | 786.98M |       2 |
|  24 | 趴懶大       | 753.84M |       2 |
|  25 | LordGiga     | 621.02M |       4 |
|  26 | Azrael       | 607.42M |       1 |
|  27 | brfc         | 573.85M |       1 |
|  28 | Pikachu      | 472.67M |       2 |
|  29 | Trimute      | 421.21M |       3 |
|  30 | Ukel         | 377.78M |       2 |
|  31 | 차은아       | 360.37M |       4 |
|  32 | Shabazz      | 351.52M |       2 |
|  33 | King Koopa   | 223.74M |       2 |
|  34 | Lord Keith   | 200.80M |       1 |
|  35 | Kay_forshort | 193.20M |       1 |
|  36 | The KING TUT | 164.43M |       2 |
|  37 | XLR8R        | 115.52M |       1 |
|  38 | Doon         |  84.96M |       2 |
|  39 | BelalShash   |  29.15M |       1 |
|  40 | Supernova    |  26.73M |       1 |
|  41 | 熾星空       |  14.12M |       1 |

<!-- [[[end]]] -->

</details>
