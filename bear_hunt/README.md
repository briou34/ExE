# 🐻 Bear Hunt

Keeping only the last 7 records, which is the number of bear hunts in between two Castle Battles.

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

<!-- [[[end]]] -->

<!-- [[[cog
# Display the latest bear damages bar graph
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_bear1_damages\.png")
imgs_dir = Path("bear_hunt", "images")
graph_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![Bear 1 damages graph]({Path('images') / graph_fpath.name})")
]]] -->

![Bear 1 damages graph](images/2025-10-30_bear1_damages.png)

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

![Bear 2 damages graph](images/2025-10-30_bear2_damages.png)

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
|   1 | 達努巴克         |   3.17B |       7 |
|   2 | Coma             |   2.42B |       7 |
|   3 | IrotRiot         |   1.87B |       7 |
|   4 | Sjefen           |   1.84B |       7 |
|   5 | Troka            |   1.82B |       7 |
|   6 | Lyghtz           |   1.76B |       4 |
|   7 | Lloyd Frontera   |   1.55B |       7 |
|   8 | FallingRegrets   |   1.45B |       7 |
|   9 | Briou            |   1.21B |       7 |
|  10 | LadyLove         |   1.12B |       6 |
|  11 | Cery             | 820.86M |       2 |
|  12 | Monkey D Ciuscon | 758.67M |       6 |
|  13 | Dossari          | 744.76M |       3 |
|  14 | Lord_DJ          | 743.44M |       5 |
|  15 | Brett Sinclair   | 573.37M |       5 |
|  16 | Sir Bishop       | 572.74M |       7 |
|  17 | DarthPorpoise    | 565.86M |       4 |
|  18 | BlackBebe        | 541.88M |       3 |
|  19 | DarkPanda        | 498.53M |       4 |
|  20 | MOnsTruM224      | 457.79M |       5 |
|  21 | rice baby        | 420.57M |       4 |
|  22 | Mill2y           | 418.13M |       1 |
|  23 | Lord Adoniran    | 308.09M |       2 |
|  24 | Queen of Cats    | 286.31M |       2 |
|  25 | LEA              | 274.83M |       7 |
|  26 | Aziz             | 241.11M |       1 |
|  27 | sin6969          | 196.32M |       1 |
|  28 | Darth Porpoise   | 195.76M |       2 |
|  29 | Queen of Hearts  | 187.87M |       2 |
|  30 | Thadeus          | 182.90M |       2 |
|  31 | 熾星空           | 165.92M |       1 |
|  32 | ROSTR            | 164.15M |       2 |
|  33 | 少量課金者       | 128.02M |       1 |
|  34 | Cloney Jr        | 127.40M |       1 |
|  35 | Kings Scooby     | 116.87M |       1 |
|  36 | RainbowMonkey    | 110.06M |       2 |
|  37 | Trimute          | 102.02M |       2 |
|  38 | 趴懶大           |  99.74M |       3 |
|  39 | TheGuardiaN      |  94.62M |       1 |
|  40 | Sked             |  91.34M |       1 |
|  41 | HasannEmree      |  90.72M |       1 |
|  42 | DoRaeMi          |  73.78M |       1 |
|  43 | BelalShash       |  64.59M |       2 |
|  44 | Morphose         |  59.26M |       1 |
|  45 | Dumblidore       |  56.27M |       2 |
|  46 | EL MACHO         |  55.38M |       1 |
|  47 | MAKO             |  55.11M |       2 |
|  48 | Forsaken         |  54.23M |       1 |
|  49 | KW               |  48.90M |       1 |
|  50 | PangolaPapi      |  31.09M |       1 |
|  51 | ALFADHLI         |  30.23M |       2 |
|  52 | Sensio           |  25.85M |       1 |
|  53 | Montanas         |  21.88M |       1 |
|  54 | Nubian King 13   |   9.21M |       1 |
|  55 | 球球仔           |   2.65M |       1 |

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

|   # | Player          |   Score | # Hunts |
| --: | :-------------- | ------: | ------: |
|   1 | Frinkley        |   6.94B |       7 |
|   2 | Chen            |   6.73B |       7 |
|   3 | Ocram           |   5.14B |       7 |
|   4 | Yaaak           |   4.72B |       7 |
|   5 | Aziz            |   3.75B |       6 |
|   6 | TW              |   2.77B |       6 |
|   7 | Fear            |   2.47B |       6 |
|   8 | Rage            |   1.71B |       7 |
|   9 | HuiMin          |   1.63B |       7 |
|  10 | brfc            |   1.47B |       5 |
|  11 | Shell           |   1.36B |       6 |
|  12 | TIBBI           |   1.32B |       3 |
|  13 | Azrael          |   1.31B |       7 |
|  14 | Lyghtz          |   1.30B |       2 |
|  15 | Kings Scooby    | 983.68M |       4 |
|  16 | 少量課金者      | 944.75M |       4 |
|  17 | DoRaeMi         | 715.78M |       4 |
|  18 | SP1R1T          | 694.65M |       4 |
|  19 | TheGuardiaN     | 619.89M |       4 |
|  20 | Dazzl           | 610.20M |       2 |
|  21 | BlackBebe       | 590.43M |       2 |
|  22 | 屁屁俠          | 528.62M |       5 |
|  23 | 趴懶大          | 509.52M |       2 |
|  24 | Sked            | 432.02M |       3 |
|  25 | Shabazz         | 360.68M |       3 |
|  26 | Queen of Hearts | 354.00M |       2 |
|  27 | Professor       | 344.51M |       1 |
|  28 | 球球仔          | 318.09M |       3 |
|  29 | Cloney Jr       | 307.09M |       2 |
|  30 | scorpion        | 302.65M |       6 |
|  31 | LordGiga        | 272.38M |       4 |
|  32 | Antonio         | 249.72M |       3 |
|  33 | Willow          | 241.82M |       2 |
|  34 | Mill2y          | 232.29M |       1 |
|  35 | DarkPanda       | 196.80M |       2 |
|  36 | tamere          | 177.77M |       1 |
|  37 | Queen of Cats   | 139.38M |       1 |
|  38 | Supernova       | 137.10M |       1 |
|  39 | LauRa Che       | 121.83M |       1 |
|  40 | Lady Emily      | 106.11M |       2 |
|  41 | Ukel            | 100.57M |       3 |
|  42 | HasannEmree     |  96.55M |       1 |
|  43 | Mazzoni         |  79.07M |       2 |
|  44 | Nightmare Lune  |  69.79M |       1 |
|  45 | King Koopa      |  56.66M |       2 |
|  46 | Kenpachi        |  48.37M |       1 |
|  47 | Diablo          |  41.94M |       1 |
|  48 | KW              |  37.38M |       1 |
|  49 | supernova       |  37.08M |       1 |
|  50 | SARAH           |  17.79M |       1 |
|  51 | ROSTR           |  15.22M |       1 |
|  52 | 차은아          |  13.72M |       1 |
|  53 | PangolaPapi     |  11.26M |       1 |
|  54 | ALFADHLI        |   4.22M |       1 |

<!-- [[[end]]] -->
