import pyperclip, time

previous = pyperclip.paste()


try:
    while True:
        current = pyperclip.paste()
        if current != previous:
            print(current)
            previous = current
        time.sleep(0.01)
except:
    pass
