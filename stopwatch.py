import time

def getHHMMSS(seconds: float) -> tuple[int, int, float]:
    ss = round(seconds % 60, 2)
    mm = int((seconds // 60) % 60)
    hh = int(seconds // (60 * 60))
    return (hh, mm, ss)


start = time.time()

try:
    lap_counter = 1
    first_time = time.time()
    lap_start = first_time
    while True:
        input(f"Lap {lap_counter}")
        total_seconds = round(time.time() - first_time, 2)
        lap_seconds = round(time.time() - lap_start, 2)
        total_time = getHHMMSS(total_seconds)
        lap_time = getHHMMSS(lap_seconds)
        print(f"Total Time: {total_time[0]}:{total_time[1]}:{total_time[2]}", end=" | ")
        print(f"Lap Time: {lap_time[0]}:{lap_time[1]}:{lap_time[2]}")
        lap_counter += 1
        lap_start = time.time()
except KeyboardInterrupt:
    print()
