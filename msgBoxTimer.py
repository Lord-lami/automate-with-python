import time, pymsgbox

wait_duration = float(pymsgbox.prompt("Provide the wait time in seconds"))

time.sleep(wait_duration)

pymsgbox.alert("Time's UP!")