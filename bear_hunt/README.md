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
| 2025-10-24 | 23 | 5.23B |
| 2025-10-26 | 27 | 4.62B |

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
| 2025-10-26 | 18 | 7.66B |

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
| 1 | 達努巴克 | 3.32B | 7 |
| 2 | Coma | 2.55B | 7 |
| 3 | Troka | 1.91B | 7 |
| 4 | Sjefen | 1.86B | 7 |
| 5 | IrotRiot | 1.71B | 7 |
| 6 | Lyghtz | 1.70B | 4 |
| 7 | Lloyd Frontera | 1.59B | 7 |
| 8 | FallingRegrets | 1.38B | 7 |
| 9 | Cery | 1.27B | 3 |
| 10 | Briou | 1.10B | 7 |
| 11 | LadyLove | 1.06B | 6 |
| 12 | Dossari | 934.44M | 4 |
| 13 | Lord_DJ | 884.34M | 6 |
| 14 | Monkey D Ciuscon | 836.68M | 6 |
| 15 | BlackBebe | 715.48M | 3 |
| 16 | Brett Sinclair | 573.37M | 5 |
| 17 | Sir Bishop | 560.01M | 7 |
| 18 | rice baby | 550.72M | 5 |
| 19 | MOnsTruM224 | 518.96M | 5 |
| 20 | DarkPanda | 467.91M | 4 |
| 21 | Mill2y | 418.13M | 1 |
| 22 | DarthPorpoise | 410.93M | 3 |
| 23 | Lord Adoniran | 345.88M | 3 |
| 24 | Queen of Hearts | 313.99M | 3 |
| 25 | Darth Porpoise | 277.07M | 3 |
| 26 | Aziz | 241.11M | 1 |
| 27 | LEA | 210.65M | 6 |
| 28 | sin6969 | 196.32M | 1 |
| 29 | Professor | 190.99M | 1 |
| 30 | 熾星空 | 165.92M | 1 |
| 31 | ROSTR | 164.15M | 2 |
| 32 | Sked | 151.52M | 2 |
| 33 | Dazzl | 150.56M | 1 |
| 34 | 少量課金者 | 128.02M | 1 |
| 35 | Cloney Jr | 127.40M | 1 |
| 36 | Queen of Cats | 121.83M | 1 |
| 37 | Kings Scooby | 116.87M | 1 |
| 38 | RainbowMonkey | 110.06M | 2 |
| 39 | Trimute | 102.02M | 2 |
| 40 | Azrael | 95.26M | 1 |
| 41 | TheGuardiaN | 94.62M | 1 |
| 42 | HasannEmree | 90.72M | 1 |
| 43 | Thadeus | 78.76M | 1 |
| 44 | DoRaeMi | 73.78M | 1 |
| 45 | 趴懶大 | 72.99M | 2 |
| 46 | BelalShash | 64.59M | 2 |
| 47 | Dumblidore | 56.27M | 2 |
| 48 | EL MACHO | 55.38M | 1 |
| 49 | MAKO | 51.73M | 1 |
| 50 | KW | 48.90M | 1 |
| 51 | PangolaPapi | 31.09M | 1 |
| 52 | ALFADHLI | 30.23M | 2 |
| 53 | Sensio | 25.85M | 1 |
| 54 | Montanas | 21.88M | 1 |
| 55 | Shabazz | 19.67M | 1 |
| 56 | Nubian King 13 | 9.21M | 1 |
| 57 | 球球仔 | 2.65M | 1 |

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
| 1 | Chen | 6.55B | 7 |
| 2 | Frinkley | 6.17B | 6 |
| 3 | Ocram | 5.32B | 7 |
| 4 | Yaaak | 4.68B | 7 |
| 5 | Aziz | 3.37B | 6 |
| 6 | TW | 3.13B | 6 |
| 7 | Fear | 2.39B | 6 |
| 8 | brfc | 1.76B | 5 |
| 9 | Shell | 1.55B | 6 |
| 10 | HuiMin | 1.48B | 6 |
| 11 | Rage | 1.47B | 7 |
| 12 | Lyghtz | 1.30B | 2 |
| 13 | 趴懶大 | 1.17B | 4 |
| 14 | Azrael | 1.08B | 5 |
| 15 | 屁屁俠 | 719.83M | 6 |
| 16 | SP1R1T | 713.16M | 4 |
| 17 | TheGuardiaN | 665.13M | 4 |
| 18 | DoRaeMi | 618.27M | 4 |
| 19 | Dazzl | 610.20M | 2 |
| 20 | BlackBebe | 590.43M | 2 |
| 21 | 球球仔 | 511.90M | 3 |
| 22 | 少量課金者 | 508.32M | 2 |
| 23 | TIBBI | 504.89M | 1 |
| 24 | Kings Scooby | 468.78M | 2 |
| 25 | Sked | 432.02M | 3 |
| 26 | Only you | 415.52M | 2 |
| 27 | Shabazz | 360.68M | 3 |
| 28 | Queen of Hearts | 354.00M | 2 |
| 29 | Professor | 344.51M | 1 |
| 30 | Antonio | 338.33M | 5 |
| 31 | LordGiga | 309.51M | 4 |
| 32 | Willow | 241.82M | 2 |
| 33 | scorpion | 232.74M | 6 |
| 34 | Mill2y | 232.29M | 1 |
| 35 | Cloney Jr | 220.46M | 1 |
| 36 | DarkPanda | 196.80M | 2 |
| 37 | Mazzoni | 177.96M | 2 |
| 38 | tamere | 177.77M | 1 |
| 39 | Queen of Cats | 139.38M | 1 |
| 40 | Supernova | 137.10M | 1 |
| 41 | Ukel | 125.29M | 4 |
| 42 | LauRa Che | 121.83M | 1 |
| 43 | HasannEmree | 96.55M | 1 |
| 44 | 차은아 | 80.53M | 2 |
| 45 | Nightmare Lune | 69.79M | 1 |
| 46 | King Koopa | 66.11M | 3 |
| 47 | ROSTR | 54.35M | 2 |
| 48 | supernova | 37.08M | 1 |
| 49 | 17 | 20.60M | 1 |
| 50 | SARAH | 17.79M | 1 |
| 51 | PangolaPapi | 11.26M | 1 |
| 52 | Nubian King 13 | 3.68M | 1 |
| 53 | Morphose | 1.02M | 1 |
| 54 | LEA | 580.49K | 1 |

<!-- [[[end]]] -->
