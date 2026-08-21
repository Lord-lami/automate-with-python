import sys, pyperclip, webbrowser, bs4

address = ""
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

map_search_link = f"https://www.openstreetmap.org/search?query={address}"

webbrowser.open(map_search_link)
