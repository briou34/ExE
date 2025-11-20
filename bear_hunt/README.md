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

![Bear Participation](images/2025-11-20_hive_participation.png)

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

![Bear Participation](images/2025-11-20_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2025-11-20_bear1_damages.png)

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
|   1 | 達努巴克         |   7.07B |       6 |
|   2 | Lyghtz           |   5.61B |       6 |
|   3 | Coma             |   4.17B |       6 |
|   4 | Troka            |   4.10B |       6 |
|   5 | Llyod Frontera   |   4.09B |       7 |
|   6 | Cery             |   3.97B |       4 |
|   7 | Sjefen           |   3.80B |       6 |
|   8 | Briou            |   3.67B |       7 |
|   9 | LadyLove         |   3.42B |       7 |
|  10 | FallingRegrets   |   2.84B |       6 |
|  11 | IrotRiot         |   2.41B |       4 |
|  12 | Darth Porpoise   |   1.95B |       6 |
|  13 | CiusconUnchained |   1.65B |       5 |
|  14 | DarkPanda        |   1.48B |       7 |
|  15 | Mill2y           |   1.40B |       3 |
|  16 | Queen of Hearts  |   1.12B |       5 |
|  17 | Queen of Cats    | 996.06M |       4 |
|  18 | LEA              | 879.56M |       5 |
|  19 | Sir Bishop       | 783.10M |       6 |
|  20 | KALON            | 674.66M |       3 |
|  21 | Lord_DJ          | 459.33M |       2 |
|  22 | MOnsTruM224      | 432.36M |       3 |
|  23 | Azrael           | 411.80M |       2 |
|  24 | Thadeus          | 337.10M |       2 |
|  25 | Lord Adoniran    | 316.33M |       1 |
|  26 | Supernova        | 261.98M |       2 |
|  27 | Dumblidore       | 225.91M |       2 |
|  28 | HasannEmree      | 188.80M |       1 |
|  29 | Morphose         | 173.83M |       2 |
|  30 | Professor        | 158.13M |       1 |
|  31 | 屁屁俠           | 147.12M |       1 |
|  32 | MOnsTrUM224      | 123.18M |       1 |
|  33 | Kenpachi         | 113.76M |       1 |
|  34 | Trimute          | 111.30M |       1 |
|  35 | LongBow3rd       |  83.81M |       1 |
|  36 | Monyahcat        |  83.32M |       1 |
|  37 | BelalShash       |  61.95M |       1 |
|  38 | King of Dogs     |  60.83M |       1 |
|  39 | ROSTR            |  59.73M |       1 |
|  40 | 趴懶大           |  51.04M |       1 |
|  41 | Mazzoni          |  36.95M |       1 |
|  42 | Dumbildore       |  31.47M |       1 |
|  43 | Brett Sinclair   |  26.88M |       1 |
|  44 | King Koopa       |  21.10M |       1 |
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

![Bear 2 damages graph](images/2025-11-20_bear2_damages.png)

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
|   1 | CHEN陈           |  10.79B |       7 |
|   2 | Ocram            |   8.25B |       7 |
|   3 | Frinkley         |   7.96B |       5 |
|   4 | Aziz             |   6.55B |       7 |
|   5 | TW拍吉           |   5.19B |       7 |
|   6 | DoRaeMi          |   3.92B |       7 |
|   7 | Fear             |   3.75B |       5 |
|   8 | Yaaak            |   3.61B |       3 |
|   9 | HuiMin           |   2.74B |       7 |
|  10 | Rage             |   2.63B |       5 |
|  11 | brfc             |   2.49B |       5 |
|  12 | 球球仔           |   2.08B |       7 |
|  13 | Shell            |   2.03B |       5 |
|  14 | Brett Sinclair   |   2.02B |       4 |
|  15 | Brica            |   1.96B |       5 |
|  16 | Sked             |   1.71B |       6 |
|  17 | Azrael           |   1.56B |       5 |
|  18 | SP1R1T           |   1.49B |       6 |
|  19 | Kings Scooby     |   1.25B |       4 |
|  20 | Lord_DJ          |   1.16B |       3 |
|  21 | Cery             |   1.09B |       1 |
|  22 | 屁屁俠           | 982.59M |       5 |
|  23 | 少量課金者       | 969.96M |       3 |
|  24 | Professor        | 805.64M |       1 |
|  25 | Kenpachi         | 755.13M |       3 |
|  26 | scorpion         | 707.81M |       3 |
|  27 | 趴懶大           | 639.88M |       4 |
|  28 | Sjefen           | 610.65M |       1 |
|  29 | TIBBI            | 539.84M |       1 |
|  30 | Saiint           | 317.91M |       3 |
|  31 | Ukel             | 317.80M |       5 |
|  32 | Shabazz          | 314.42M |       2 |
|  33 | Diablo           | 287.11M |       1 |
|  34 | Trimute          | 223.49M |       3 |
|  35 | 차은아           | 205.79M |       1 |
|  36 | Morphose         | 191.45M |       1 |
|  37 | tamere           | 187.51M |       1 |
|  38 | CiusconUnchained | 178.42M |       1 |
|  39 | LEA              | 138.28M |       1 |
|  40 | LordGiga         | 124.70M |       3 |
|  41 | Doon             |  40.56M |       2 |
|  42 | LongBow3rd       |  39.02M |       1 |
|  43 | The KING TUT     |  31.32M |       2 |
|  44 | Nightmare Lune   |  20.25M |       1 |
|  45 | Lady Emily       |  17.00M |       1 |
|  46 | I am your father |  15.81M |       1 |
|  47 | 熾星空           |  12.29M |       1 |
|  48 | Nubian King 13   |   9.56M |       1 |
|  49 | HASANNEMREE      |   8.67M |       1 |
|  50 | XLR8R            |   7.05M |       1 |

<!-- [[[end]]] -->

</details>
