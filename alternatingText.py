import pyperclip

input("Copy the text that you want to change the case to aLtErNaTiNg case and press ENTER")

text = pyperclip.paste()

upper_case = False

result = ""

for char in text:
    if upper_case:
        result += char.upper()
    else:
        result += char.lower()
    upper_case = not upper_case
pyperclip.copy(result)
        