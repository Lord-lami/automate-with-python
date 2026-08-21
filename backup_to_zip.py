# backup_to_zip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments

import zipfile, os
from pathlib import Path

def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = Path(folder)  # Make sure folder is a Path object, not string.

    # Figure out the ZIP filename this code should use, based on
    # what files already exist.
    number = 1
    zip_filename = ""
    while True:

        zip_filename = Path(folder.parts[-1] + '_' + str(number) + '.zip')
        if not zip_filename.exists():
            break
        number = number + 1

    # TODO: Create the ZIP file.
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zip_file:


    # TODO: Walk the entire folder tree and compress the files in each folder.
        for current_dir, _, filenames in os.walk("."):
            for fn in filenames:
                zip_file.write(os.path.join(current_dir, fn))
        
    print('Done.')

backup_to_zip(Path.home() / 'spam')