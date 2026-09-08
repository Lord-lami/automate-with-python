import subprocess


subprocess.run(["sudo", "ydotool", "mousemove", "--delay", "1000", "100", "100"], capture_output=True)
subprocess.run(["sudo", "ydotool", "mousemove", "--delay", "1000", "200", "100"], capture_output=True)
subprocess.run(["sudo", "ydotool", "mousemove", "--delay", "1000", "200", "200"], capture_output=True)
subprocess.run(["sudo", "ydotool", "mousemove", "--delay", "1000", "100", "200"], capture_output=True)
