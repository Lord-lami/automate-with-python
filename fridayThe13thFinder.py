import datetime

def same_day_next_month(day: datetime.datetime) -> datetime.datetime:
    if day.month < 12:
        day = day.replace(month=day.month + 1)
    else:
        day = day.replace(month=1, year=day.year + 1)
    return day

def nextNFriday13thFinder(n: int) -> list[tuple[int, int]]:
    friday13ths = []
    day = datetime.datetime.now()
    # If the day of the month is not 13th
    if day.day != 13:
        prev_day = day.day
        # Set the day to the next 13th
        day = day.replace(day=13)
        if prev_day > 13:
            day = same_day_next_month(day)

    # Get the next 10 Friday the 13ths
    while len(friday13ths) < n:
        # If the day is Friday add it
        if day.weekday() == 4:
            friday13ths.append((day.month, day.year))
        # Move on to the next month
        day = same_day_next_month(day)
    return friday13ths

def same_day_last_month(day: datetime.datetime) -> datetime.datetime:
    if day.month > 1:
        day = day.replace(month=day.month - 1)
    else:
        day = day.replace(month=12, year=day.year - 1)
    return day

def lastNFriday13thFinder(n: int) -> list[tuple[int, int]]:
    friday13ths = []
    day = datetime.datetime.now()
    # If the day of the month is not 13th
    if day.day != 13:
        prev_day = day.day
        # Set the day to the next 13th
        day = day.replace(day=13)
        if prev_day < 13:
            day = same_day_last_month(day)

    # Get the last 10 Friday the 13ths
    while len(friday13ths) < n:
        # If the day is Friday add it
        if day.weekday() == 4:
            friday13ths.append((day.month, day.year))
        # Move on to the last month
        day = same_day_last_month(day)
    return friday13ths

print(nextNFriday13thFinder(5))
print(lastNFriday13thFinder(5))


