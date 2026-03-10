# Hive

<!-- [[[cog
# Display the latest hive map
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_hive\.png")
imgs_dir = Path("hive", "images")
hive_map_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![hive map]({Path('images') / hive_map_fpath.name})")
]]] -->

![hive map](images/2026-03-10_hive.png)

<!-- [[[end]]] -->

<!-- [[[cog
from datetime import datetime, UTC
from hive import get_cities_locations_table, as_markdown_table

print(f"Cities locations as of {datetime.now(UTC).strftime('%Y-%m-%d')}:\n")
print(as_markdown_table(get_cities_locations_table(), columns=["Name", "X", "Y"]))
]]] -->

Cities locations as of 2026-03-10:

| Name             | X   | Y   |
| ---------------- | --- | --- |
| AZIZ             | 716 | 543 |
| Aqua             | 727 | 554 |
| Aqua_Too         | 722 | 556 |
| AussieJosh       | 731 | 553 |
| Azrael           | 735 | 553 |
| Batas            | 735 | 551 |
| Bori             | 726 | 546 |
| Brgy TIBAY       | 723 | 548 |
| Brica            | 733 | 551 |
| Briou            | 718 | 544 |
| CHEN陈           | 730 | 545 |
| Cavendish        | 708 | 545 |
| Cery             | 713 | 549 |
| Coma             | 717 | 550 |
| CravenMoorehead  | 721 | 552 |
| Creamy Dangles   | 740 | 559 |
| DarkPanda        | 711 | 549 |
| DeathAmongstUs   | 715 | 554 |
| Diablo           | 724 | 544 |
| Donald Porpoise  | 718 | 546 |
| Donut            | 738 | 559 |
| Dossari          | 717 | 554 |
| Ellie Softpaw    | 709 | 547 |
| EmmyLou          | 719 | 552 |
| FallingRegrets   | 715 | 552 |
| Fear             | 735 | 547 |
| FireGOW          | 735 | 549 |
| Frinkley         | 728 | 546 |
| George Floyd     | 734 | 543 |
| Hawkeye          | 728 | 556 |
| Helzu            | 721 | 554 |
| Heney            | 733 | 547 |
| HuiMin           | 733 | 549 |
| JoeyBootzz       | 719 | 550 |
| KESHKERES        | 716 | 541 |
| KR4V3N           | 728 | 544 |
| Kay_forshort     | 711 | 552 |
| Kenpachi         | 723 | 550 |
| Kenz             | 713 | 551 |
| King Koopa       | 719 | 554 |
| Kings Scooby     | 729 | 552 |
| LEA              | 711 | 547 |
| Lady KimmyKakes  | 727 | 550 |
| LadyLove         | 714 | 543 |
| Lagertha         | 709 | 541 |
| Lest             | 728 | 541 |
| Llyod Frontera   | 712 | 545 |
| Lord Adoniran    | 712 | 543 |
| Lord Peanut      | 722 | 544 |
| Lord Shen        | 737 | 549 |
| LordGiga         | 729 | 554 |
| LordOfTheKinguin | 720 | 540 |
| Lord_DJ          | 725 | 550 |
| Lyghtz           | 714 | 545 |
| M E D U S A      | 717 | 552 |
| MOnsTruM224      | 721 | 550 |
| Malideiter       | 727 | 558 |
| MasterkinG32     | 725 | 554 |
| Meow             | 737 | 552 |
| MeowAndOnly      | 737 | 554 |
| Morphose         | 727 | 552 |
| Mr Bean          | 738 | 541 |
| Ocram            | 728 | 548 |
| Paerdekop        | 713 | 547 |
| PapiChurro       | 720 | 544 |
| Persian Gulf     | 726 | 556 |
| Queen of Hearts  | 721 | 548 |
| Rage             | 726 | 548 |
| SARAH            | 722 | 540 |
| SP1R1T           | 732 | 543 |
| SSE              | 726 | 542 |
| Saint Xitar      | 718 | 542 |
| Shabazz          | 737 | 543 |
| Shadow           | 731 | 551 |
| Shamalamaba      | 729 | 558 |
| Shell2y          | 719 | 548 |
| Sir Bishop       | 720 | 546 |
| Sjefen           | 716 | 545 |
| Sked             | 726 | 544 |
| Soraaa           | 730 | 556 |
| Supernova        | 718 | 540 |
| TW拍吉           | 732 | 545 |
| The Bob          | 734 | 541 |
| The Jordinator   | 738 | 545 |
| Trimute          | 722 | 546 |
| Troka            | 715 | 550 |
| Velvet Sins      | 710 | 545 |
| Vitvik           | 729 | 550 |
| Wancho           | 737 | 547 |
| Willow           | 723 | 554 |
| Yanta            | 736 | 556 |
| alusia           | 736 | 541 |
| destro           | 725 | 552 |
| lord270927633    | 726 | 540 |
| mary             | 713 | 541 |
| scorpion         | 730 | 541 |
| tamere           | 733 | 553 |
| vinfinity        | 736 | 545 |
| 帕殿咚           | 730 | 543 |
| 熾星空           | 720 | 542 |
| 球球仔           | 734 | 545 |
| 趴懶大           | 724 | 546 |
| 하루&까망        | 732 | 541 |

<!-- [[[end]]] -->
