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

![hive map](images/2025-10-27_hive.png)

<!-- [[[end]]] -->

<!-- [[[cog
from datetime import datetime, UTC
from hive import get_cities_locations_table, as_markdown_table

print(f"Cities locations as of {datetime.now(UTC).strftime('%Y-%m-%d')}:\n")
print(as_markdown_table(get_cities_locations_table(), columns=["Name", "X", "Y"]))
]]] -->

Cities locations as of 2025-10-27:

| Name | X | Y |
| --- | --- | --- |
| ALFADHLI | 713 | 541 |
| Aziz | 728 | 544 |
| Azrael | 735 | 553 |
| BlackBebe | 733 | 549 |
| Brett Sinclair | 713 | 553 |
| Briou | 711 | 547 |
| CHEN陈 | 730 | 545 |
| Cery | 712 | 545 |
| Cloney Jr | 738 | 551 |
| Coma | 719 | 550 |
| DarkPanda | 725 | 554 |
| Darth Porpoise | 716 | 543 |
| Diablo | 738 | 545 |
| DoRaeMi | 726 | 546 |
| Dossari | 717 | 550 |
| Dumblidore | 713 | 551 |
| FallingRegrets | 715 | 552 |
| Fear | 734 | 545 |
| Forsaken | 709 | 549 |
| Frinkley | 728 | 546 |
| GUNNAR | 735 | 547 |
| HuiMin | 732 | 543 |
| HᴀꜱᴀɴɴEᴍʀᴇᴇ | 723 | 548 |
| Ibra | 734 | 541 |
| IronFLS | 736 | 545 |
| IrotRiot | 720 | 546 |
| Kai forshort | 723 | 554 |
| Kenpachi | 737 | 553 |
| King Koopa | 724 | 544 |
| Kings Scooby | 729 | 552 |
| LEA | 722 | 544 |
| Lady Emily | 716 | 541 |
| LadyLove | 714 | 543 |
| Lloyd Frontera | 712 | 543 |
| LongBow3rd | 709 | 541 |
| Lord Adoniran | 713 | 549 |
| Lord Keith | 708 | 545 |
| LordGiga | 729 | 554 |
| Lord_DJ | 725 | 550 |
| Lyghtz | 714 | 545 |
| MIHAWK | 726 | 540 |
| MOnsTruM224 | 719 | 554 |
| Mazzoni | 726 | 544 |
| Mill2y | 718 | 544 |
| Mk 21_03 | 739 | 549 |
| Monkey D Ciuscon | 717 | 552 |
| Montanas | 717 | 554 |
| Monyahcat | 733 | 553 |
| Morphose | 727 | 552 |
| MurderMittens | 709 | 543 |
| Nick | 719 | 548 |
| Nightmare Lune | 732 | 541 |
| Nubian King 13 | 725 | 552 |
| Ocram | 728 | 548 |
| PangolaPapi | 720 | 544 |
| Professor | 735 | 549 |
| Queen of Cats | 711 | 549 |
| Queen of Hearts | 721 | 548 |
| ROSTR | 731 | 553 |
| Rage | 726 | 548 |
| RainbowMonkey | 723 | 552 |
| SARAH | 722 | 541 |
| SP1R1T | 726 | 542 |
| Sensio | 721 | 554 |
| Shabazz | 723 | 550 |
| Shell | 731 | 551 |
| Sir Bishop | 710 | 545 |
| Sjefen | 713 | 547 |
| Sked | 737 | 549 |
| Supernova | 724 | 546 |
| TIBBI | 727 | 550 |
| TW拍吉 | 732 | 545 |
| Thadeus | 709 | 547 |
| TheGuardiaN | 735 | 551 |
| Trimute | 722 | 546 |
| Troka | 715 | 550 |
| Ukel | 724 | 557 |
| Willow | 711 | 554 |
| XLR8R | 713 | 539 |
| Yaaak | 733 | 547 |
| brfc | 733 | 551 |
| rice baby | 721 | 552 |
| scorpion | 730 | 541 |
| sin6969 | 718 | 546 |
| tamere | 727 | 554 |
| ابو فهد KW | 728 | 541 |
| 少量課金者 | 736 | 542 |
| 屁屁俠 | 730 | 543 |
| 是17呀 | 737 | 547 |
| 熾星空 | 718 | 542 |
| 球球仔 | 734 | 543 |
| 趴懶大 | 729 | 550 |
| 達努巴克 | 716 | 545 |
| 차은아 | 730 | 556 |

<!-- [[[end]]] -->
