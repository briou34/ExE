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

![Bear Participation](images/2025-11-25_hive_participation.png)

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

![Bear Participation](images/2025-11-25_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2025-11-25_bear1_damages.png)

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
|   1 | 達努巴克         |   6.59B |       6 |
|   2 | Lyghtz           |   6.06B |       6 |
|   3 | Coma             |   4.48B |       6 |
|   4 | Cery             |   4.20B |       4 |
|   5 | Llyod Frontera   |   4.19B |       7 |
|   6 | Briou            |   3.79B |       7 |
|   7 | Troka            |   3.49B |       6 |
|   8 | Sjefen           |   3.38B |       5 |
|   9 | LadyLove         |   3.33B |       7 |
|  10 | FallingRegrets   |   2.57B |       6 |
|  11 | CiusconUnchained |   2.18B |       6 |
|  12 | IrotRiot         |   2.16B |       3 |
|  13 | DarkPanda        |   1.85B |       7 |
|  14 | Darth Porpoise   |   1.45B |       5 |
|  15 | LEA              |   1.27B |       6 |
|  16 | Queen of Cats    |   1.14B |       4 |
|  17 | Queen of Hearts  |   1.11B |       4 |
|  18 | Lord_DJ          |   1.09B |       3 |
|  19 | Sir Bishop       | 871.29M |       6 |
|  20 | Mill2y           | 845.46M |       2 |
|  21 | KALON            | 674.66M |       3 |
|  22 | Azrael           | 450.05M |       1 |
|  23 | Brica            | 435.64M |       1 |
|  24 | Aziz             | 430.38M |       1 |
|  25 | MOnsTrUM224      | 334.47M |       2 |
|  26 | MOnsTruM224      | 321.23M |       2 |
|  27 | Lord Adoniran    | 316.33M |       1 |
|  28 | Morphose         | 173.83M |       2 |
|  29 | Professor        | 158.13M |       1 |
|  30 | 屁屁俠           | 147.12M |       1 |
|  31 | Supernova        | 116.03M |       2 |
|  32 | Kay_forshort     | 115.21M |       1 |
|  33 | Kenpachi         | 113.76M |       1 |
|  34 | LongBow3rd       |  83.81M |       1 |
|  35 | Monyahcat        |  83.32M |       1 |
|  36 | ROSTR            |  79.67M |       3 |
|  37 | Dumblidore       |  64.56M |       2 |
|  38 | BelalShash       |  61.95M |       1 |
|  39 | King of Dogs     |  60.83M |       1 |
|  40 | 趴懶大           |  51.04M |       1 |
|  41 | Mazzoni          |  36.95M |       1 |
|  42 | 차은아           |  21.18M |       1 |
|  43 | King Koopa       |  21.10M |       1 |
|  44 | Thadeus          |   6.69M |       1 |
|  45 | Mk 21_03         |   4.14M |       1 |

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

![Bear 2 damages graph](images/2025-11-25_bear2_damages.png)

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
|   1 | CHEN陈           |  11.38B |       7 |
|   2 | Ocram            |  10.25B |       7 |
|   3 | Frinkley         |   8.58B |       5 |
|   4 | Aziz             |   6.13B |       6 |
|   5 | TW拍吉           |   5.02B |       7 |
|   6 | DoRaeMi          |   4.63B |       7 |
|   7 | Brett Sinclair   |   3.90B |       6 |
|   8 | Fear             |   3.75B |       5 |
|   9 | Rage             |   3.50B |       6 |
|  10 | brfc             |   3.20B |       5 |
|  11 | HuiMin           |   3.16B |       7 |
|  12 | 球球仔           |   2.39B |       7 |
|  13 | Yaaak            |   2.32B |       2 |
|  14 | Brica            |   2.22B |       6 |
|  15 | SP1R1T           |   2.06B |       6 |
|  16 | Azrael           |   2.05B |       6 |
|  17 | 屁屁俠           |   1.40B |       5 |
|  18 | Sked             |   1.34B |       5 |
|  19 | 少量課金者       |   1.24B |       3 |
|  20 | Kings Scooby     |   1.14B |       3 |
|  21 | Cery             |   1.09B |       1 |
|  22 | Shell            |   1.05B |       3 |
|  23 | 趴懶大           | 874.31M |       4 |
|  24 | Professor        | 843.37M |       1 |
|  25 | Scorpion         | 842.18M |       1 |
|  26 | Kenpachi         | 755.13M |       3 |
|  27 | Lord_DJ          | 748.44M |       2 |
|  28 | Sjefen           | 624.50M |       2 |
|  29 | tamere           | 622.31M |       2 |
|  30 | Saiint           | 502.62M |       4 |
|  31 | scorpion         | 431.63M |       2 |
|  32 | Shabazz          | 314.42M |       2 |
|  33 | Ukel             | 303.93M |       5 |
|  34 | Diablo           | 287.11M |       1 |
|  35 | Morphose         | 278.56M |       2 |
|  36 | CiusconUnchained | 178.42M |       1 |
|  37 | Queen of Hearts  | 176.24M |       1 |
|  38 | Trimute          | 127.90M |       2 |
|  39 | Nubian King 13   | 106.57M |       2 |
|  40 | The KING TUT     |  57.35M |       3 |
|  41 | Doon             |  40.56M |       2 |
|  42 | 熾星空           |  37.29M |       2 |
|  43 | Lord Adoniran    |  21.39M |       1 |
|  44 | Nightmare Lune   |  20.25M |       1 |
|  45 | Lady Emily       |  17.00M |       1 |
|  46 | Lord Keith       |  11.59M |       1 |
|  47 | HASANNEMREE      |   8.67M |       1 |
|  48 | XLR8R            |   7.05M |       1 |
|  49 | 차은아           |   2.24M |       1 |
|  50 | LordGiga         |   2.21M |       1 |

<!-- [[[end]]] -->

</details>
