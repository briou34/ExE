# 🐻 Bear Hunt

Keeping only the last 7 records, which is the number of bear hunts in between two Castle Battles.

## Participation

<!-- [[[cog
# Display the latest bear damages bar graph
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_hive_participation\.png")
imgs_dir = Path("bear_hunt", "images")
graph_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![Bear Participation]({Path('images') / graph_fpath.name})")
]]] -->
<!-- [[[end]]] -->


## Summary

**Bear 1:**

<!-- [[[cog
from analysis import summary, as_markdown_table
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

<!-- [[[end]]] -->

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

![Bear 1 damages graph](images/2025-11-08_bear1_damages.png)

<!-- [[[end]]] -->

**Bear 2:**

<!-- [[[cog
from analysis import summary, as_markdown_table
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

<!-- [[[end]]] -->

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

![Bear 2 damages graph](images/2025-11-08_bear2_damages.png)

<!-- [[[end]]] -->

## Bear 1 - Top Players over last 7 hunts

<!-- [[[cog
from analysis import players_records, as_markdown_table
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
|   1 | 達努巴克         |   4.45B |       7 |
|   2 | Lyghtz           |   4.11B |       7 |
|   3 | Troka            |   2.63B |       7 |
|   4 | Llyod Frontera   |   2.41B |       7 |
|   5 | IrotRiot         |   2.36B |       7 |
|   6 | Coma             |   2.34B |       6 |
|   7 | FallingRegrets   |   2.29B |       7 |
|   8 | LadyLove         |   2.16B |       7 |
|   9 | Cery             |   2.05B |       3 |
|  10 | Briou            |   1.76B |       7 |
|  11 | Sjefen           |   1.50B |       6 |
|  12 | Darth Porpoise   |   1.43B |       6 |
|  13 | BlackBebe        |   1.35B |       5 |
|  14 | DarkPanda        | 933.13M |       7 |
|  15 | CiusconUnchained | 912.57M |       6 |
|  16 | Queen of Cats    | 852.06M |       5 |
|  17 | Lord_DJ          | 765.03M |       4 |
|  18 | Brett Sinclair   | 665.13M |       5 |
|  19 | MOnsTruM224      | 640.80M |       7 |
|  20 | Sir Bishop       | 546.24M |       6 |
|  21 | Mill2y           | 529.54M |       1 |
|  22 | LEA              | 493.47M |       7 |
|  23 | Queen of Hearts  | 488.67M |       3 |
|  24 | Professor        | 456.47M |       2 |
|  25 | Lord Adoniran    | 440.15M |       2 |
|  26 | Thadeus          | 434.55M |       2 |
|  27 | HasannEmree      | 352.14M |       2 |
|  28 | Dossari          | 296.95M |       2 |
|  29 | Trimute          | 294.32M |       3 |
|  30 | Azrael           | 250.36M |       1 |
|  31 | King of Dogs     | 223.89M |       3 |
|  32 | Dumblidore       | 206.77M |       2 |
|  33 | Supernova        | 158.14M |       1 |
|  34 | SARAH            | 130.93M |       1 |
|  35 | Morphose         | 128.51M |       2 |
|  36 | ROSTR            | 128.35M |       2 |
|  37 | Diablo           | 118.18M |       1 |
|  38 | Kings Scooby     | 116.87M |       1 |
|  39 | XLR8R            |  69.74M |       1 |
|  40 | sin6969          |  55.62M |       1 |
|  41 | MAKO             |  55.11M |       2 |
|  42 | 趴懶大           |  48.26M |       2 |
|  43 | BelalShash       |  38.00M |       1 |
|  44 | rice baby        |  29.13M |       1 |
|  45 | Teddix           |  27.49M |       1 |
|  46 | Ukel             |  15.41M |       1 |
|  47 | sin666           |   2.93M |       1 |

<!-- [[[end]]] -->

## Bear 2 - Top Players over last 7 hunts

<!-- [[[cog
from analysis import players_records, as_markdown_table
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
|   1 | CHEN陈           |   6.57B |       7 |
|   2 | Frinkley         |   4.36B |       5 |
|   3 | Ocram            |   4.35B |       7 |
|   4 | Aziz             |   4.15B |       7 |
|   5 | TW拍吉           |   3.48B |       7 |
|   6 | Yaaak            |   3.23B |       5 |
|   7 | 少量課金者       |   1.93B |       7 |
|   8 | Fear             |   1.79B |       5 |
|   9 | brfc             |   1.76B |       6 |
|  10 | TIBBI            |   1.75B |       4 |
|  11 | DoRaeMi          |   1.72B |       5 |
|  12 | Shell            |   1.66B |       6 |
|  13 | HuiMin           |   1.65B |       7 |
|  14 | Rage             |   1.25B |       5 |
|  15 | Azrael           |   1.16B |       6 |
|  16 | Professor        | 884.40M |       2 |
|  17 | SP1R1T           | 863.76M |       4 |
|  18 | TheGuardiaN      | 767.91M |       5 |
|  19 | Sked             | 637.92M |       3 |
|  20 | Kings Scooby     | 621.81M |       3 |
|  21 | Cery             | 459.69M |       1 |
|  22 | 屁屁俠           | 456.84M |       4 |
|  23 | Lord_DJ          | 451.65M |       2 |
|  24 | 球球仔           | 424.13M |       6 |
|  25 | 趴懶大           | 372.55M |       3 |
|  26 | scorpion         | 346.35M |       5 |
|  27 | King Scooby      | 333.51M |       1 |
|  28 | Cloney Jr        | 307.09M |       2 |
|  29 | LordGiga         | 245.84M |       4 |
|  30 | 차은아           | 213.43M |       2 |
|  31 | Diablo           | 211.77M |       2 |
|  32 | 屁屁侠           | 194.03M |       1 |
|  33 | Queen of Hearts  | 184.53M |       1 |
|  34 | Trimute          | 177.14M |       2 |
|  35 | Shabazz          | 140.53M |       1 |
|  36 | Ukel             | 127.87M |       1 |
|  37 | Lady Emily       | 106.11M |       2 |
|  38 | HasannEmree      |  96.55M |       1 |
|  39 | Monyahcat        |  80.21M |       1 |
|  40 | ROSTR            |  69.43M |       1 |
|  41 | EL MACHO         |  66.83M |       1 |
|  42 | Mazzoni          |  55.34M |       2 |
|  43 | Kenpachi         |  48.37M |       1 |
|  44 | LongBow3rd       |  39.02M |       1 |
|  45 | ابو فهد KW       |  37.38M |       1 |
|  46 | supernova        |  37.08M |       1 |
|  47 | The KING TUT     |  34.95M |       2 |
|  48 | MAKO             |  21.65M |       1 |
|  49 | PangolaPapi      |  17.99M |       1 |
|  50 | I am your father |  15.81M |       1 |
|  51 | tamere           |  14.77M |       1 |
|  52 | Nightmare Lune   |  11.61M |       1 |
|  53 | ALFADHLI         |   4.22M |       1 |

<!-- [[[end]]] -->
