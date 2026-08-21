import time, os, copy, send2trash
from pathlib import Path

def seconds_to_days(seconds: float) -> float:
    return seconds / (24 * 60 * 60)

excluded_dirs = {"./venv"}

def compile_excluded_dirs():
    exdirs = copy.copy(excluded_dirs)
    for dir in exdirs:
        for dirname, subdirs, _ in os.walk(dir):
            for dir in subdirs:
                excluded_dirs.add(dirname + "/" + dir)

compile_excluded_dirs()
# print(excluded_dirs)

def getFilesNotUsedInTheLast(amount_of_days: float) -> list[Path]:
    chopping_block = []
    for current_dir, _, filenames in os.walk("."):
        if current_dir in excluded_dirs:
            continue
        for fn in filenames:
            filepath = Path(current_dir) / fn
            unused_days = seconds_to_days(time.time() - filepath.stat().st_atime)
            if unused_days > amount_of_days:
                chopping_block.append(filepath)
    return chopping_block


# print(*getFilesNotUsedInTheLast(1), sep="\n")

def getFilesLargerThan(max_size_bytes: int) -> list[Path]:
    chopping_block = []
    for current_dir, _, filenames in os.walk("."):
        if current_dir in excluded_dirs:
            continue
        for fn in filenames:
            filepath = Path(current_dir) / fn
            size = filepath.stat().st_size
            if size > max_size_bytes:
                chopping_block.append(filepath)
    return chopping_block

print(*getFilesLargerThan(1024), sep="\n")

def deleteAll(files: list[Path]):
    for f in files:
        send2trash.send2trash(f)


# file_stats = Path("fizzBuzzNumber.py").stat()
# unused_days = seconds_to_days(time.time() - file_stats.st_ctime)

# print(unused_days, "days")
# print("Size:", file_stats.st_size)