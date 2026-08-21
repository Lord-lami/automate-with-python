import pyperclip, sys
from pathlib import Path

modifier = "."
if len(sys.argv) > 1:
    modifier = sys.argv[1]

back_steps = len(modifier.split("/"))
cwd = Path.cwd().absolute()

if not back_steps < len(cwd.parts):
    print(f"Compared to the current folder depth there are too many backwards steps in modifer:", modifier, file=sys.stderr)
    print("exiting with status 1")
    sys.exit(1)

if modifier == ".":
    pyperclip.copy(str(cwd))
elif modifier == ".." + ("/.." * (back_steps - 1)):
    path_list = cwd.parts[:-back_steps]
    pyperclip.copy(path_list[0] + "/".join(path_list[1:]))
else:
    print("Invalid modifer after ccwd:", modifier, file=sys.stderr)
    print("exiting with status 1")
    sys.exit(1)
