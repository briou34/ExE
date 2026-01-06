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

![hive map](hive/images/2026-01-06_hive.png)

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

______________________________________________________________________

- Tue 06 Jan - Today (Day 184)

______________________________________________________________________

- Mon 12 Jan - 🏆 Strongest Governor IV (Day 190)
- Sat 17 Jan - 🏰 Castle Fight (Day 195)
- Mon 19 Jan - ✨ Gen 4 Heroes (Day 197)
- Mon 19 Jan - 🐶 Gen 4 Pets (Day 197)
- Mon 26 Jan - ⚔ KvK V (Day 204)
- Sat 31 Jan - 🏰 Castle Fight (Day 209)
- Mon 16 Feb - 🏫 War Academy (Day 225)
- Mon 23 Feb - ⚔ KvK VI (Day 232)
- Mon 23 Mar - ⚔ KvK VII (Day 260)
- Mon 20 Apr - ⚔ KvK VIII (Day 288)

<!-- [[[end]]] -->
