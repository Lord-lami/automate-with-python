import pyperclip

input("Copy a list that you want to add bullet points to and press enter...")

raw_list = pyperclip.paste()

lines = raw_list.split("\n")

bullet_list = ""

for line in lines:
    bullet_list += "* " + line + "\n"

pyperclip.copy(bullet_list)

print("The bullet pointed list below has been saved to the clip board")

print(bullet_list)


