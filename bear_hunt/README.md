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

| Date | # Players | Total score |
| :--- | ---: | ---: |
| 2025-10-12 | 30 | 5.97B |
| 2025-10-14 | 27 | 4.86B |
| 2025-10-16 | 24 | 3.05B |
| 2025-10-18 | 20 | 2.75B |
| 2025-10-20 | 23 | 3.82B |
| 2025-10-22 | 28 | 6.03B |

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

| Date | # Players | Total score |
| :--- | ---: | ---: |
| 2025-10-12 | 22 | 5.53B |
| 2025-10-14 | 24 | 7.03B |
| 2025-10-17 | 25 | 5.54B |
| 2025-10-19 | 23 | 9.44B |
| 2025-10-21 | 28 | 10.03B |
| 2025-10-23 | 28 | 7.12B |

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

| # | Player | Score | # Hunts |
| ---: | :--- | ---: | ---: |
| 1 | 達努巴克 | 2.75B | 6 |
| 2 | Coma | 2.22B | 6 |
| 3 | Sjefen | 1.72B | 6 |
| 4 | Troka | 1.53B | 6 |
| 5 | Lloyd Frontera | 1.45B | 6 |
| 6 | Cery | 1.35B | 3 |
| 7 | Lyghtz | 1.32B | 3 |
| 8 | IrotRiot | 1.31B | 6 |
| 9 | FallingRegrets | 1.21B | 6 |
| 10 | Dossari | 1.13B | 5 |
| 11 | Briou | 902.10M | 6 |
| 12 | Lord_DJ | 809.78M | 5 |
| 13 | Monkey D Ciuscon | 643.87M | 5 |
| 14 | rice baby | 521.59M | 4 |
| 15 | BlackBebe | 517.83M | 2 |
| 16 | LadyLove | 491.74M | 4 |
| 17 | Queen of Hearts | 464.09M | 3 |
| 18 | Darth Porpoise | 439.83M | 4 |
| 19 | Mill2y | 418.13M | 1 |
| 20 | Lord Adoniran | 412.23M | 3 |
| 21 | Sir Bishop | 388.98M | 6 |
| 22 | MOnsTruM224 | 352.82M | 4 |
| 23 | Dazzl | 310.93M | 2 |
| 24 | Nick | 296.50M | 1 |
| 25 | Brett Sinclair | 261.25M | 3 |
| 26 | Azrael | 259.00M | 2 |
| 27 | Aziz | 241.11M | 1 |
| 28 | Sked | 226.05M | 3 |
| 29 | Shell | 223.90M | 1 |
| 30 | DarkPanda | 210.50M | 2 |
| 31 | sin6969 | 196.32M | 1 |
| 32 | Professor | 190.99M | 1 |
| 33 | 少量課金者 | 128.02M | 1 |
| 34 | Cloney Jr | 127.40M | 1 |
| 35 | Dark Panda | 123.45M | 1 |
| 36 | DarthPorpoise | 123.30M | 1 |
| 37 | LEA | 122.39M | 5 |
| 38 | HasannEmree | 122.07M | 2 |
| 39 | Queen of Cats | 121.83M | 1 |
| 40 | RainbowMonkey | 110.06M | 2 |
| 41 | TheGuardiaN | 94.62M | 1 |
| 42 | 熾星空 | 87.31M | 1 |
| 43 | Thadeus | 78.76M | 1 |
| 44 | DoRaeMi | 73.78M | 1 |
| 45 | Dumblidore | 56.27M | 2 |
| 46 | EL MACHO | 55.38M | 1 |
| 47 | KW | 48.90M | 1 |
| 48 | Trimute | 40.73M | 1 |
| 49 | BelalShash | 37.87M | 2 |
| 50 | PangolaPapi | 31.09M | 1 |
| 51 | ALFADHLI | 30.23M | 2 |
| 52 | Sensio | 25.85M | 1 |
| 53 | Montanas | 21.88M | 1 |
| 54 | Shabazz | 19.67M | 1 |
| 55 | Supernova | 16.72M | 1 |
| 56 | MikeE2005 | 11.35M | 1 |
| 57 | Nubian King 13 | 9.21M | 1 |
| 58 | 球球仔 | 2.65M | 1 |

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

| # | Player | Score | # Hunts |
| ---: | :--- | ---: | ---: |
| 1 | Chen | 5.54B | 6 |
| 2 | Frinkley | 4.94B | 5 |
| 3 | Ocram | 4.51B | 6 |
| 4 | Yaaak | 4.02B | 6 |
| 5 | Aziz | 2.69B | 5 |
| 6 | Fear | 2.39B | 6 |
| 7 | TW | 2.36B | 5 |
| 8 | brfc | 1.38B | 4 |
| 9 | Lyghtz | 1.30B | 2 |
| 10 | Shell | 1.28B | 5 |
| 11 | Rage | 1.20B | 6 |
| 12 | 趴懶大 | 1.17B | 4 |
| 13 | HuiMin | 1.12B | 5 |
| 14 | Azrael | 745.05M | 4 |
| 15 | SP1R1T | 713.16M | 4 |
| 16 | TheGuardiaN | 665.13M | 4 |
| 17 | DoRaeMi | 618.27M | 4 |
| 18 | 屁屁俠 | 614.69M | 5 |
| 19 | Dazzl | 610.20M | 2 |
| 20 | BlackBebe | 590.43M | 2 |
| 21 | 球球仔 | 511.90M | 3 |
| 22 | TIBBI | 504.89M | 1 |
| 23 | Kings Scooby | 468.78M | 2 |
| 24 | Sked | 432.02M | 3 |
| 25 | Only you | 415.52M | 2 |
| 26 | Shabazz | 360.68M | 3 |
| 27 | Queen of Hearts | 354.00M | 2 |
| 28 | Professor | 344.51M | 1 |
| 29 | Antonio | 338.33M | 5 |
| 30 | LordGiga | 249.75M | 3 |
| 31 | Willow | 241.82M | 2 |
| 32 | Mill2y | 232.29M | 1 |
| 33 | 少量課金者 | 222.79M | 1 |
| 34 | DarkPanda | 196.80M | 2 |
| 35 | Mazzoni | 177.96M | 2 |
| 36 | tamere | 177.77M | 1 |
| 37 | scorpion | 157.08M | 5 |
| 38 | Queen of Cats | 139.38M | 1 |
| 39 | Supernova | 137.10M | 1 |
| 40 | Ukel | 125.29M | 4 |
| 41 | LauRa Che | 121.83M | 1 |
| 42 | 차은아 | 80.53M | 2 |
| 43 | Nightmare Lune | 69.79M | 1 |
| 44 | King Koopa | 66.11M | 3 |
| 45 | ROSTR | 54.35M | 2 |
| 46 | 17 | 20.60M | 1 |
| 47 | SARAH | 17.79M | 1 |
| 48 | PangolaPapi | 11.26M | 1 |
| 49 | Nubian King 13 | 3.68M | 1 |
| 50 | Morphose | 1.02M | 1 |
| 51 | LEA | 580.49K | 1 |

<!-- [[[end]]] -->
