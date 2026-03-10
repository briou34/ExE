# ExE

- [Hive](hive/README.md)
- [Bear Hunt](bear_hunt/README.md)
- [Timeline](#timeline)

## Hive

<!-- [[[cog
# Display the latest hive map
import re
from pathlib import Path
pattern = re.compile(r"(\d{4}-\d{2}-\d{2})_hive\.png")
imgs_dir = Path("hive", "images")
hive_map_fpath = sorted(
  [fpath for fpath in imgs_dir.iterdir() if pattern.match(fpath.name)]
)[-1]
print(f"![hive map]({hive_map_fpath})")
]]] -->

![hive map](hive/images/2026-03-10_hive.png)

<!-- [[[end]]] -->

## Timeline

<!-- [[[cog
from timeline import make_timeline
timeline = make_timeline()
for line in timeline:
    print(line)
]]] -->

- Mon 07 Jul - Server launch (Day 1)
- Mon 06 Oct - ⚔ KvK I (Day 92)
- Mon 27 Oct - ✨ Gen 3 Heroes (Day 113)
- Mon 27 Oct - 🐶 Gen 3 Pets (Day 113)
- Mon 03 Nov - ⚔ KvK II (Day 120)
- Mon 01 Dec - ⚔ KvK III (Day 148)
- Mon 08 Dec - 📦 True Gold 5 (Day 155)
- Mon 29 Dec - ⚔ KvK IV (Day 176)
- Sun 04 Jan - 🔄 Transfer #1 (Day 182)
- Mon 19 Jan - ✨ Gen 4 Heroes (Day 197)
- Mon 19 Jan - 🐶 Gen 4 Pets (Day 197)
- Mon 26 Jan - ⚔ KvK V (Day 204)
- Mon 16 Feb - 🎭 Season 5 (Day 225)
- Mon 16 Feb - 🏫 War Academy (Day 225)
- Mon 23 Feb - ⚔ KvK VI (Day 232)
- Sun 01 Mar - 🔄 Transfer #2 (Day 238)

______________________________________________________________________

- Tue 10 Mar - Today (Day 247)

______________________________________________________________________

- Sat 14 Mar - 🏰 Castle Fight (Day 251)
- Mon 23 Mar - ⚔ KvK VII (Day 260)
- Tue 24 Mar - 🍀 Roulette #5 (Day 261)
- Sat 28 Mar - 🏰 Castle Fight (Day 265)
- Mon 06 Apr - 🏆 Strongest Governor VII (Day 274)
- Tue 07 Apr - 🍀 Roulette #6 (Day 275)
- Mon 13 Apr - 🎭 Season 6 (Day 281)
- Mon 13 Apr - ✨ Gen 5 Heroes (Day 281)
- Mon 13 Apr - 🐶 Gen 5 Pets (Day 281)
- Mon 20 Apr - ⚔ KvK VIII (Day 288)
- Sun 26 Apr - 🔄 Transfer #3 (Day 294)
- Mon 18 May - 🦸 True Gold 8 (Day 316)
- Mon 18 May - ⚔ KvK IX (Day 316)
- Mon 15 Jun - ⚔ KvK X (Day 344)
- Sun 21 Jun - 🔄 Transfer #4 (Day 350)
- Mon 22 Jun - ✨ Gen 6 Heroes (Day 351)
- Mon 22 Jun - 🐶 Gen 6 Pets (Day 351)
- Sun 16 Aug - 🔄 Transfer #5 (Day 406)

<!-- [[[end]]] -->
