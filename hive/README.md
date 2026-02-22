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

![hive map](images/2026-02-22_hive.png)

<!-- [[[end]]] -->

<!-- [[[cog
from datetime import datetime, UTC
from hive import get_cities_locations_table, as_markdown_table

print(f"Cities locations as of {datetime.now(UTC).strftime('%Y-%m-%d')}:\n")
print(as_markdown_table(get_cities_locations_table(), columns=["Name", "X", "Y"]))
]]] -->

Cities locations as of 2026-02-22:

| Name             | X   | Y   |
| ---------------- | --- | --- |
| ALFADHLI         | 713 | 553 |
| AZIZ             | 716 | 543 |
| AussieJosh       | 729 | 550 |
| Azrael           | 735 | 553 |
| BlockZ           | 709 | 543 |
| Blossom          | 738 | 559 |
| Bori             | 726 | 546 |
| Brica            | 733 | 551 |
| Briou            | 718 | 544 |
| CHEN陈           | 730 | 545 |
| Cavendish        | 708 | 545 |
| Cery             | 713 | 549 |
| CiusPorpoise     | 719 | 550 |
| Cloney Jr        | 737 | 552 |
| Coma             | 717 | 550 |
| DarkPanda        | 711 | 549 |
| DeathAmongstUs   | 715 | 554 |
| Diablo           | 724 | 544 |
| Donald Porpoise  | 720 | 538 |
| Dossari          | 717 | 554 |
| Dunndertaker     | 709 | 552 |
| EmmyLou          | 719 | 552 |
| FallingRegrets   | 715 | 552 |
| Fear             | 735 | 547 |
| FireGOW          | 735 | 549 |
| Frinkley         | 728 | 546 |
| George Floyd     | 709 | 554 |
| HASANNEMREE      | 723 | 552 |
| Hawkeye          | 728 | 556 |
| HuiMin           | 733 | 549 |
| I am your father | 711 | 554 |
| IrotRiot         | 718 | 546 |
| JoeyBootzz       | 717 | 552 |
| KOREA장태욱      | 722 | 544 |
| KR4V3N           | 728 | 544 |
| Kay_forshort     | 711 | 552 |
| Kenpachi         | 723 | 550 |
| Kenz             | 713 | 551 |
| King Koopa       | 719 | 554 |
| Kings Scooby     | 729 | 552 |
| KittyCopia       | 726 | 542 |
| LEA              | 711 | 547 |
| LadyLove         | 714 | 543 |
| LightsOutL       | 715 | 539 |
| Llyod Frontera   | 712 | 545 |
| Loading          | 734 | 543 |
| Lord Adoniran    | 712 | 543 |
| Lord Morpheus    | 730 | 556 |
| LordGiga         | 729 | 554 |
| LordOfTheKinguin | 720 | 540 |
| Lord_DJ          | 725 | 550 |
| Lou_Scunt        | 721 | 552 |
| Lyghtz           | 714 | 545 |
| M E D U S A      | 709 | 549 |
| MOnsTruM224      | 721 | 550 |
| MasterkinG32     | 725 | 554 |
| Morphose         | 727 | 552 |
| Nubian King 13   | 725 | 552 |
| O D I N          | 718 | 542 |
| Ocram            | 728 | 548 |
| Paerdekop        | 713 | 547 |
| Pain             | 710 | 545 |
| PapiChurro       | 720 | 544 |
| Persian Gulf     | 726 | 556 |
| Ppap             | 737 | 549 |
| Queen of Hearts  | 721 | 548 |
| ROSTR            | 723 | 554 |
| Rage             | 726 | 548 |
| SARAH            | 722 | 541 |
| SP1R1T           | 732 | 543 |
| Shabazz          | 737 | 543 |
| Shadow           | 733 | 547 |
| Shell2y          | 719 | 548 |
| Sir Bishop       | 720 | 546 |
| Sjefen           | 716 | 545 |
| Sked             | 726 | 544 |
| Soraaa           | 736 | 545 |
| Supernova        | 724 | 546 |
| TW拍吉           | 732 | 545 |
| Thadeus          | 722 | 539 |
| The Bob          | 734 | 541 |
| Tiffany          | 716 | 541 |
| Trillbill        | 721 | 554 |
| Trimute          | 722 | 546 |
| Troka            | 715 | 550 |
| Ukel             | 727 | 554 |
| Willow           | 734 | 555 |
| alusia           | 736 | 541 |
| mary             | 713 | 541 |
| maxee            | 737 | 554 |
| scorpion         | 730 | 541 |
| tamere           | 733 | 553 |
| vinfinity        | 727 | 550 |
| yacob            | 723 | 548 |
| 帕殿咚           | 730 | 543 |
| 熾星空           | 720 | 542 |
| 球球仔           | 734 | 545 |
| 趴懶大           | 731 | 551 |
| 達努巴克         | 740 | 559 |
| 하루&까망        | 732 | 541 |

<!-- [[[end]]] -->
