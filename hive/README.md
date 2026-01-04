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

![hive map](images/2026-01-04_hive.png)

<!-- [[[end]]] -->

<!-- [[[cog
from datetime import datetime, UTC
from hive import get_cities_locations_table, as_markdown_table

print(f"Cities locations as of {datetime.now(UTC).strftime('%Y-%m-%d')}:\n")
print(as_markdown_table(get_cities_locations_table(), columns=["Name", "X", "Y"]))
]]] -->

Cities locations as of 2026-01-04:

| Name             | X   | Y   |
| ---------------- | --- | --- |
| ALFADHLI         | 721 | 550 |
| Aziz             | 728 | 544 |
| Azrael           | 735 | 553 |
| BelalShash       | 738 | 559 |
| Big Poppa 24     | 739 | 549 |
| BlackBebe        | 713 | 553 |
| BlockZ           | 709 | 543 |
| Blossom          | 711 | 552 |
| Bob              | 734 | 559 |
| Bori             | 726 | 546 |
| Brica            | 733 | 551 |
| Briou            | 718 | 544 |
| BrutalB          | 740 | 559 |
| CHEN陈           | 730 | 545 |
| Cavendish        | 708 | 545 |
| Cery             | 713 | 549 |
| CiusconUnchained | 719 | 550 |
| Cloney Jr        | 737 | 552 |
| Coma             | 717 | 550 |
| DarkPanda        | 719 | 552 |
| Darth Porpoise   | 716 | 543 |
| Diablo           | 724 | 544 |
| Doon             | 734 | 541 |
| Dossari          | 717 | 554 |
| Dumblidore       | 713 | 551 |
| FallingRegrets   | 715 | 552 |
| Fear             | 734 | 545 |
| Frinkley         | 728 | 546 |
| HasannEmree      | 723 | 552 |
| Hawkeye          | 728 | 556 |
| HuiMin           | 733 | 549 |
| I am your father | 711 | 554 |
| IrotRiot         | 718 | 546 |
| KOREA장태욱      | 720 | 544 |
| Kay_forshort     | 721 | 556 |
| Kenpachi         | 723 | 550 |
| King of Dogs     | 709 | 549 |
| Kings Scooby     | 729 | 552 |
| Kjs722           | 721 | 554 |
| LEA              | 711 | 547 |
| Lady Emily       | 716 | 541 |
| LadyLove         | 714 | 543 |
| Llyod Frontera   | 712 | 545 |
| Lord Adoniran    | 712 | 543 |
| Lord Morpheus    | 730 | 556 |
| LordGiga         | 729 | 554 |
| Lord_DJ          | 725 | 550 |
| Luo              | 722 | 540 |
| Lyghtz           | 714 | 545 |
| MOMO2005         | 732 | 541 |
| MOnsTruM224      | 719 | 554 |
| MasterkinG32     | 725 | 554 |
| Mazzoni          | 726 | 542 |
| Morphose         | 727 | 552 |
| Nubian King 13   | 725 | 552 |
| Ocram            | 728 | 548 |
| Persian Gulf     | 726 | 556 |
| Ppap             | 729 | 550 |
| Queen of Cats    | 711 | 549 |
| Queen of Hearts  | 719 | 548 |
| ROSTR            | 723 | 554 |
| Rage             | 726 | 548 |
| SARAH            | 722 | 544 |
| SP1R1T           | 732 | 543 |
| Saiint           | 731 | 553 |
| Shabazz          | 737 | 543 |
| Shadow           | 733 | 547 |
| Shakieee         | 736 | 559 |
| Shell2y          | 713 | 547 |
| Sir Bishop       | 720 | 546 |
| Sjefen           | 739 | 547 |
| Sked             | 726 | 544 |
| Supernova        | 724 | 546 |
| Sweapin          | 720 | 540 |
| TW拍吉           | 732 | 545 |
| Thadeus          | 709 | 547 |
| The KING TUT     | 723 | 548 |
| TrillBill        | 710 | 545 |
| Trimute          | 722 | 546 |
| Troka            | 715 | 550 |
| Ukel             | 721 | 548 |
| Willow           | 719 | 556 |
| XLR8R            | 713 | 539 |
| alusia           | 736 | 541 |
| mary             | 713 | 541 |
| maxee            | 734 | 555 |
| scorpion         | 730 | 541 |
| tamere           | 733 | 553 |
| yacob            | 737 | 547 |
| 屁屁俠           | 730 | 543 |
| 熾星空           | 718 | 542 |
| 球球仔           | 734 | 543 |
| 趴懶大           | 731 | 551 |
| 達努巴克         | 716 | 545 |
| 차은아           | 736 | 545 |

<!-- [[[end]]] -->
