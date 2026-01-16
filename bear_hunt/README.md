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

![Bear Participation](images/2026-01-16_hive_participation.png)

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

![Bear Participation](images/2026-01-16_hive_participation_moving.png)

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

![Bear 1 damages graph](images/2026-01-16_bear1_damages.png)

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
|   1 | Coma             |   9.12B |       7 |
|   2 | Lyghtz           |   8.82B |       6 |
|   3 | Troka            |   7.83B |       6 |
|   4 | LadyLove         |   7.51B |       7 |
|   5 | Llyod Frontera   |   7.02B |       7 |
|   6 | Briou            |   6.78B |       7 |
|   7 | Paerdekop        |   6.26B |       4 |
|   8 | Cery             |   4.98B |       5 |
|   9 | DarkPanda        |   4.97B |       7 |
|  10 | Shell2y          |   4.86B |       6 |
|  11 | LEA              |   4.56B |       7 |
|  12 | BadCiuSpencer    |   4.46B |       6 |
|  13 | Kenz             |   4.35B |       4 |
|  14 | IrotRiot         |   4.01B |       6 |
|  15 | Ocram            |   3.79B |       3 |
|  16 | FallingRegrets   |   3.77B |       4 |
|  17 | EmmyLou          |   3.68B |       5 |
|  18 | Queen of Hearts  |   2.95B |       4 |
|  19 | Darth Porpoise   |   2.93B |       5 |
|  20 | Sir Bishop       |   2.66B |       7 |
|  21 | M E D U S A      |   2.65B |       4 |
|  22 | Sjefen           |   2.39B |       2 |
|  23 | TheGlizzinator   |   2.36B |       4 |
|  24 | Kenpachi         |   2.24B |       3 |
|  25 | Señor Bootie     |   2.20B |       3 |
|  26 | PapiChurro       |   1.90B |       4 |
|  27 | Lord_DJ          |   1.90B |       4 |
|  28 | mary             |   1.87B |       5 |
|  29 | DeathAmongstUs   |   1.52B |       4 |
|  30 | Kay_forshort     |   1.44B |       3 |
|  31 | Trillbill        |   1.37B |       3 |
|  32 | scorpion         |   1.35B |       4 |
|  33 | Tiffany          |   1.29B |       3 |
|  34 | MOnsTruM224      |   1.15B |       3 |
|  35 | AZIZ             |   1.10B |       1 |
|  36 | O D I N          |   1.08B |       3 |
|  37 | MasterkinG32     | 794.07M |       2 |
|  38 | 帕殿咚           | 744.35M |       1 |
|  39 | JoeyBootzz       | 576.84M |       1 |
|  40 | Morphose         | 564.59M |       2 |
|  41 | 趴懶大           | 538.82M |       1 |
|  42 | Cavendish        | 514.91M |       2 |
|  43 | BlockZ           | 477.75M |       1 |
|  44 | Hawkeye          | 350.31M |       1 |
|  45 | Lord Adoniran    | 337.91M |       2 |
|  46 | yacob            | 333.20M |       2 |
|  47 | Dunndertaker     | 301.96M |       1 |
|  48 | MOnSTruM224      | 273.41M |       1 |
|  49 | StepMothers Milk | 222.71M |       1 |
|  50 | Lady Emily       | 182.58M |       1 |
|  51 | ROSTR            | 153.07M |       1 |
|  52 | Shadow           | 127.20M |       1 |
|  53 | SARAH            |  88.52M |       1 |
|  54 | Diablo           |  48.86M |       1 |
|  55 | BelalShash       |  47.41M |       1 |
|  56 | BlackBebe        |  20.25M |       1 |
|  57 | Nubian King 13   |   3.73M |       1 |

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

![Bear 2 damages graph](images/2026-01-16_bear2_damages.png)

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
|   1 | CHEN陈           |  11.56B |       7 |
|   2 | AZIZ             |   8.43B |       6 |
|   3 | Ocram            |   8.30B |       4 |
|   4 | Azrael           |   7.98B |       7 |
|   5 | Brica            |   6.97B |       7 |
|   6 | Shadow           |   6.77B |       6 |
|   7 | Bori             |   6.73B |       6 |
|   8 | Frinkley         |   6.68B |       4 |
|   9 | SP1R1T           |   6.39B |       7 |
|  10 | Fear             |   6.38B |       6 |
|  11 | HuiMin           |   6.29B |       6 |
|  12 | 球球仔           |   5.63B |       7 |
|  13 | KR4VEN           |   5.60B |       4 |
|  14 | 帕殿咚           |   5.11B |       6 |
|  15 | Rage             |   5.04B |       5 |
|  16 | TW拍吉           |   4.55B |       7 |
|  17 | Sjefen           |   4.52B |       4 |
|  18 | AussieJosh       |   4.16B |       3 |
|  19 | Sked             |   2.86B |       5 |
|  20 | vinfinity        |   2.63B |       4 |
|  21 | The Bob          |   2.21B |       3 |
|  22 | momo&하루        |   2.19B |       7 |
|  23 | Loading          |   2.18B |       3 |
|  24 | Hawkeye          |   1.99B |       3 |
|  25 | Persian Gulf     |   1.89B |       3 |
|  26 | Lord_DJ          |   1.73B |       3 |
|  27 | GodOfWhores      |   1.72B |       2 |
|  28 | scorpion         |   1.62B |       3 |
|  29 | 趴懶大           |   1.30B |       5 |
|  30 | Kenpachi         |   1.11B |       1 |
|  31 | Queen of Hearts  | 805.72M |       1 |
|  32 | Trimute          | 720.55M |       3 |
|  33 | tamere           | 684.72M |       2 |
|  34 | Ukel             | 517.24M |       3 |
|  35 | Ppap             | 498.42M |       1 |
|  36 | yacob            | 245.41M |       2 |
|  37 | KOREA장태욱      | 233.31M |       2 |
|  38 | LordGiga         | 201.98M |       2 |
|  39 | XLR8R            | 196.05M |       1 |
|  40 | 차은아           | 193.40M |       1 |
|  41 | 熾星空           | 164.59M |       1 |
|  42 | HASANNEMREE      | 116.77M |       1 |
|  43 | Willow           | 115.86M |       1 |
|  44 | Kings Scooby     | 100.88M |       1 |
|  45 | The KING TUT     |  97.11M |       1 |
|  46 | Lord Keith       |  58.87M |       1 |
|  47 | ROSTR            |  54.22M |       1 |
|  48 | Mazzoni          |  51.90M |       1 |
|  49 | Supernova        |  45.67M |       1 |
|  50 | maxee            |   4.35M |       1 |
|  51 | I am your father |   3.69M |       1 |

<!-- [[[end]]] -->

</details>
