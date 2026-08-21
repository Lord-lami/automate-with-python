import time, sys

maxShift, gradient = 20, -1
shift = 0
try:
    while True:
        time.sleep(0.1)
        print((" " * shift) + "********")
        if shift == 0:
            gradient = 1
        elif shift == maxShift:
            gradient = -1
        shift += gradient
except KeyboardInterrupt:
    sys.exit()