from datetime import UTC, datetime, timedelta
from itertools import count

DAY0 = datetime(2025, 7, 6, tzinfo=UTC)  # Day 1 is Mon 07 Jul 2025
TODAY = datetime.now(UTC)

WEEK = timedelta(weeks=1)
DAY = timedelta(days=1)

FMT = "%a %d %b"


def main():
    events = create_events_timeline()
    timeline = format_timeline(events)
    print("\n".join(timeline))


def make_timeline():
    events = create_events_timeline()
    return format_timeline(events)


def format_timeline(events):
    timeline = []
    for event, date in events:
        day_number = (date - DAY0).days
        if event == "Today":
            timeline.append("-" * 52)
        timeline.append(f"- {date.strftime(FMT)} - {event} (Day {day_number})")
        if event == "Today":
            timeline.append("-" * 52)
    return timeline


def create_events_timeline():
    kvk1_start = datetime(2025, 10, 6, tzinfo=UTC)
    castle_fight1 = kvk1_start + 5 * DAY
    strongest_governor_1 = kvk1_start + 2 * WEEK

    events = [
        # Landmarks
        ["Server launch", DAY0 + timedelta(days=1)],
        ["Today", TODAY],
        # Heroes
        ["✨ Gen 3 Heroes", DAY0 + timedelta(days=113)],
        ["✨ Gen 4 Heroes", DAY0 + timedelta(days=197)],
        ["✨ Gen 5 Heroes", DAY0 + timedelta(days=281)],
        ["✨ Gen 6 Heroes", DAY0 + timedelta(days=351)],  # 350-360
        # Pets
        ["🐶 Gen 3 Pets", DAY0 + timedelta(days=113)],
        ["🐶 Gen 4 Pets", DAY0 + timedelta(days=197)],
        ["🐶 Gen 5 Pets", DAY0 + timedelta(days=281)],
        ["🐶 Gen 6 Pets", DAY0 + timedelta(days=351)],
        # True Gold
        ["📦 True Gold 5", DAY0 + timedelta(days=155)],
        ["🏫 War Academy", DAY0 + timedelta(days=225)],  # ~ day 220
        ["🦸 True Gold 8", DAY0 + timedelta(days=316)],  # ~ day 310-320
        # Transfer event on March 1st, 2026, every 56 days (8 weeks)
        ["🔄 Transfer #1", datetime(2026, 1, 4, tzinfo=UTC)],
        ["🔄 Transfer #2", datetime(2026, 3, 1, tzinfo=UTC)],
        ["🔄 Transfer #3", datetime(2026, 4, 26, tzinfo=UTC)],
        ["🔄 Transfer #4", datetime(2026, 6, 21, tzinfo=UTC)],
        ["🔄 Transfer #5", datetime(2026, 8, 16, tzinfo=UTC)],
    ]

    # KvKs up until next 4 months
    for i in count(1):
        kvk_start = kvk1_start + WEEK * 4 * (i - 1)
        if (kvk_start - TODAY) > WEEK * 16:
            break
        events.append([f"⚔ KvK {roman(i)}", kvk_start])

    # Next Strongest Governor
    for i in count(1):
        sg_date = strongest_governor_1 + WEEK * 4 * (i - 1)
        if (sg_date - TODAY).days > 0:
            events.append([f"🏆 Strongest Governor {roman(i)}", sg_date])
            break

    # Next 2 Castle Fights
    for i in count(1):
        cf_date = castle_fight1 + WEEK * 2 * (i - 1)
        if (cf_date - TODAY).days < 0:
            continue
        if (cf_date - TODAY).days > 28:
            break
        events.append(["🏰 Castle Fight", cf_date])

    # Roulettes between up till next gen
    roulette_gen4_first = DAY0 + timedelta(days=205)
    next_gen = DAY0 + timedelta(days=281)
    for i in count(1):
        roulette_day = roulette_gen4_first + WEEK * 2 * (i - 1)
        if roulette_day < TODAY:
            continue
        if roulette_day > next_gen:
            break
        events.append([f"🍀 Roulette #{i}", roulette_day])
    print()

    # Add current and next season, one season each 8 weeks, starts on Wednesdays
    first_monday = DAY0 + timedelta(days=1)
    season_length = 56  # 8 weeks
    current_season = ((TODAY - first_monday).days // season_length) + 1
    current_season_start = DAY0 + timedelta(days=(current_season - 1) * season_length + 1)
    events.append([f"🎭 Season {current_season}", current_season_start])
    next_season_start = current_season_start + timedelta(days=season_length)
    events.append([f"🎭 Season {current_season + 1}", next_season_start])

    # Sort by date
    events = sorted(events, key=lambda item: (item[1], "Season" not in item[0]))

    return events


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
