import os, shutil

for dirname, _, filenames in os.walk('spam'):
    for f in filenames:
        filepath = os.path.join(dirname, f)
        uppercase_filename_path = os.path.join(dirname, f[:-4].upper()+f[-4:])
        shutil.move(filepath, uppercase_filename_path)
        # print(filepath)
        # print(uppercase_filename_path)
