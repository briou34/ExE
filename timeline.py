from datetime import UTC, datetime, timedelta
from itertools import count


def main():
    timeline = make_timeline()
    for line in timeline:
        print(line)


def make_timeline():
    fmt = "%a %d %b"
    day0 = datetime(2025, 7, 6, tzinfo=UTC)  # Day 1 is Mon 07 Jul 2025

    WEEK = timedelta(weeks=1)
    DAY = timedelta(days=1)

    today = datetime.now(UTC)
    kvk1_start = datetime(2025, 10, 6, tzinfo=UTC)
    castle_fight1 = kvk1_start + 5 * DAY
    strongest_governor_1 = kvk1_start + 2 * WEEK

    events = [
        # Landmarks
        ["Server launch", day0 + timedelta(days=1)],
        ["Today", today],
        # Heroes
        ["✨ Gen 3 Heroes", day0 + timedelta(days=112)],
        ["✨ Gen 4 Heroes early start", day0 + timedelta(days=190)],
        ["✨ Gen 4 Heroes late start", day0 + timedelta(days=200)],
        # Pets
        ["🐶 Gen 3 Pets early start", day0 + timedelta(days=105)],
        ["🐶 Gen 3 Pets late start", day0 + timedelta(days=110)],
        ["🐶 Gen 4 Pets early start", day0 + timedelta(days=190)],
        ["🐶 Gen 4 Pets late start", day0 + timedelta(days=200)],
        # True Gold
        ["📦 True Gold 5", day0 + timedelta(days=150)],
        ["🏫 War Academy", day0 + timedelta(days=220)],
    ]

    # KvKs up until next 4 months
    for i in count(1):
        kvk_start = kvk1_start + WEEK * 4 * (i - 1)
        if (kvk_start - today) > WEEK * 16:
            break
        events.append([f"⚔ KvK {roman(i)}", kvk_start])

    # Next Strongest Governor
    for i in count(1):
        sg_date = strongest_governor_1 + WEEK * 4 * (i - 1)
        if (sg_date - today).days > 0:
            events.append([f"🏆 Strongest Governor {roman(i)}", sg_date])
            break

    # Next 2 Castle Fights
    for i in count(1):
        cf_date = castle_fight1 + WEEK * 2 * (i - 1)
        if (cf_date - today).days < 0:
            continue
        if (cf_date - today).days > 20:
            break
        events.append(["🏰 Castle Fight", cf_date])

    # Sort by date
    events = sorted(events, key=lambda item: item[1])

    timeline = []
    for event, date in events:
        day_number = (date - day0).days
        if event == "Today":
            timeline.append("-" * 52)
        timeline.append(f"- {date.strftime(fmt)} - {event} (Day {day_number})")
        if event == "Today":
            timeline.append("-" * 52)

    return timeline


def roman(n):
    num = [1, 4, 5, 9, 10, 40, 50]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L"]
    i = len(num) - 1
    parts = []
    while n:
        div = n // num[i]
        n %= num[i]
        while div:
            parts.append(sym[i])
            div -= 1
        i -= 1
    return "".join(parts)


if __name__ == "__main__":
    main()
