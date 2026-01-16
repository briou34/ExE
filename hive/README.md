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

![hive map](images/2026-01-16_hive.png)

<!-- [[[end]]] -->

<!-- [[[cog
from datetime import datetime, UTC
from hive import get_cities_locations_table, as_markdown_table

print(f"Cities locations as of {datetime.now(UTC).strftime('%Y-%m-%d')}:\n")
print(as_markdown_table(get_cities_locations_table(), columns=["Name", "X", "Y"]))
]]] -->

Cities locations as of 2026-01-16:

| Name             | X   | Y   |
| ---------------- | --- | --- |
| ALFADHLI         | 721 | 550 |
| AZIZ             | 728 | 544 |
| AussieJosh       | 735 | 547 |
| Azrael           | 735 | 553 |
| BadCiuSpencer    | 719 | 550 |
| Big Poppa 24     | 739 | 549 |
| BlackBebe        | 713 | 553 |
| BlockZ           | 709 | 543 |
| Blossom          | 711 | 552 |
| Bori             | 726 | 546 |
| Brica            | 733 | 551 |
| Briou            | 718 | 544 |
| CHEN陈           | 730 | 545 |
| Cavendish        | 708 | 545 |
| Cery             | 713 | 549 |
| Cloney Jr        | 737 | 552 |
| Coma             | 717 | 550 |
| DarkPanda        | 719 | 552 |
| Darth Porpoise   | 716 | 543 |
| DeathAmongstUs   | 712 | 556 |
| Diablo           | 724 | 544 |
| Dossari          | 717 | 554 |
| Dunndertaker     | 713 | 551 |
| EmmyLou          | 714 | 556 |
| FallingRegrets   | 715 | 552 |
| Fear             | 734 | 545 |
| Frinkley         | 728 | 546 |
| GodOfWhores      | 735 | 549 |
| HASANN EMREE     | 723 | 552 |
| Hawkeye          | 728 | 556 |
| HuiMin           | 733 | 549 |
| I am your father | 711 | 554 |
| IrotRiot         | 718 | 546 |
| KOREA장태욱      | 720 | 544 |
| KR4VEN           | 735 | 551 |
| Kay_forshort     | 721 | 556 |
| Kenpachi         | 723 | 550 |
| Kenz             | 715 | 554 |
| Kings Scooby     | 729 | 552 |
| KittyRamone      | 737 | 549 |
| LEA              | 711 | 547 |
| Lady Emily       | 716 | 541 |
| LadyLove         | 714 | 543 |
| Llyod Frontera   | 712 | 545 |
| Loading          | 738 | 545 |
| Lord Adoniran    | 712 | 543 |
| Lord Morpheus    | 730 | 556 |
| LordGiga         | 729 | 554 |
| LordOfTheKinguin | 709 | 549 |
| Lord_DJ          | 725 | 550 |
| Lyghtz           | 714 | 545 |
| M E D U S A      | 709 | 551 |
| MOnsTruM224      | 719 | 554 |
| MasterkinG32     | 725 | 554 |
| Mazzoni          | 726 | 542 |
| Morphose         | 727 | 552 |
| Nubian King 13   | 725 | 552 |
| O D I N          | 718 | 542 |
| Ocram            | 728 | 548 |
| Paerdekop        | 711 | 549 |
| Pain             | 728 | 541 |
| PapiChurro       | 716 | 556 |
| Persian Gulf     | 726 | 556 |
| Ppap             | 729 | 550 |
| Queen of Hearts  | 719 | 548 |
| ROSTR            | 723 | 554 |
| Rage             | 726 | 548 |
| SARAH            | 722 | 544 |
| SP1R1T           | 732 | 543 |
| Saiint           | 731 | 553 |
| Señor Bootie     | 717 | 552 |
| Shabazz          | 737 | 543 |
| Shadow           | 733 | 547 |
| Shell2y          | 713 | 547 |
| Sir Bishop       | 720 | 546 |
| Sjefen           | 716 | 545 |
| Sked             | 726 | 544 |
| StepMothers Milk | 709 | 541 |
| Supernova        | 724 | 546 |
| TW拍吉           | 732 | 545 |
| Thadeus          | 709 | 547 |
| The Bob          | 734 | 541 |
| TheGlizzinator   | 721 | 552 |
| Tiffany          | 718 | 540 |
| Trillbill        | 710 | 545 |
| Trimute          | 722 | 546 |
| Troka            | 715 | 550 |
| Ukel             | 721 | 548 |
| Willow           | 719 | 556 |
| XLR8R            | 713 | 539 |
| alusia           | 736 | 541 |
| mary             | 713 | 541 |
| maxee            | 737 | 557 |
| momo&하루        | 732 | 541 |
| scorpion         | 730 | 541 |
| tamere           | 733 | 553 |
| vinfinity        | 727 | 550 |
| yacob            | 737 | 547 |
| 帕殿咚           | 730 | 543 |
| 熾星空           | 720 | 542 |
| 球球仔           | 734 | 543 |
| 趴懶大           | 731 | 551 |
| 達努巴克         | 740 | 559 |
| 차은아           | 736 | 545 |

<!-- [[[end]]] -->
