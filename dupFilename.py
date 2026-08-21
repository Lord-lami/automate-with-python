import os, sys
from pathlib import Path

def dup_filenames(folder: str | Path) -> dict[str, list[Path]]:
    filenames_2_path = dict()
    dup_filenames_2_path = dict()
    for current_dir, _, filenames in os.walk(folder):
        for fn in filenames:
            if fn in filenames_2_path.keys():
                if fn in dup_filenames_2_path.keys():
                    dup_filenames_2_path[fn].append(Path(current_dir) / fn)
                else:
                    dup_filenames_2_path[fn] = [filenames_2_path[fn], Path(current_dir) / fn]
            else:
                filenames_2_path[fn] = Path(current_dir) / fn
    return dup_filenames_2_path

dups = dup_filenames("./Class_1")

for fn, paths in dups.items():
    print(fn)
    for p in paths:
        print("\t", p)
    print()

print("Running", __file__)
print("With", sys.executable, sys.version)
print("On", os.name, sys.platform)