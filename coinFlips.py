import random,logging
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
def flip_coin() -> bool:
    return random.randint(0, 1) == 1

def x_flips(x: int) -> list[bool]:
    assert x > 0
    flips = []
    for _ in range(x):
        flips.append(flip_coin())
    return flips

def streak_present(streak_size: int, flips: list[bool]) -> bool:
    assert streak_size > 0
    assert len(flips) >= streak_size
    for i in range(len(flips)-streak_size):
        if flips[i:i+streak_size] == [True] * streak_size \
        or flips[i:i+streak_size] == [False] * streak_size:
            logging.debug(str(i) + "-" + str(i+streak_size))
            return True
    return False

sample_size = 100
flips_size = 10
streak_size = 6
present_count = 0
for i in range(sample_size):
    if streak_present(streak_size, x_flips(flips_size)):
        logging.debug("Present in 100 Flips: " + str(i))
        present_count += 1

print("Streaks of 6 or more Heads or Tails were present ", (present_count/sample_size) * 100, "percent of the time")
print("Streaks of 6 or more Heads or Tails appeared", present_count, "times")