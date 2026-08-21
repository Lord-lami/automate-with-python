import time, sys

gradient, spikeSideWidth = 2, 9
lineIncrease = -1
lineLength = 1
lineCount, lcGradient = 0, -1
try:
    while True:
        print("-" * lineLength)
        # print(lineIncrease)
        if lineCount == spikeSideWidth or lineCount == 0:
            lineIncrease *= -1
            lineIncrease += gradient
            lcGradient *= -1

        lineLength += lineIncrease
        lineIncrease += gradient
        lineCount += lcGradient
        time.sleep(0.1)
        
except:
    sys.exit()