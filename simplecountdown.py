import sys, time, subprocess, pymsgbox

if len(sys.argv) > 1:
    duration = int(sys.argv[1])
else:
    print("No duration specified", file=sys.stderr)
    sys.exit(1)

if duration < 0:
    print("Negative durations are invalid", file=sys.stderr)
    sys.exit(2)
width = len(str(duration))
for second in range(duration, 0, -1):
    print(f"{second:<{width}}\r", end="")
    time.sleep(1)
print(0)
# subprocess.run(['open', 'alarm.wav'])
pymsgbox.alert("Time's Up!")
