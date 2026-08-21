import re
from pathlib import Path

print("Search your current folder with a regular expression")
regex = input()
searchRe = re.compile(regex)

print()
filepaths = list(Path.cwd().glob("*"))

print(f"Searching current folder: {Path.cwd()} ...")
for filepath in filepaths:
    found = False
    if filepath.is_dir():
        continue
    with open(filepath) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            matching = searchRe.search(line)
            if matching:
                if not found:
                    found = True
                    print(f"\tFound in file: {filepath.name}:")
                print(f"\t\tLine {i+1}: {line[:matching.start()]}\033[31m{line[matching.start():matching.end()]}\033[0m{line[matching.end():]}")
