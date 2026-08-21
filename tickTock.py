import time
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

def tick_tock(seconds):
    while seconds > 1:
        time.sleep(1)
        print("Tick...")
        time.sleep(1)
        print("Tock...")
        seconds -= 2
    if seconds == 1:
        time.sleep(1)
        print("Tick...")

tick_tock(4)

