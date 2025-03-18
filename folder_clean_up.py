#For this project, I’ll be creating a Python script that automates the organization of files and folders in a
#user-specified directory – a kind of "digital janitor", if you will.

from pathlib import Path
import shutil

#validation logic for path

while True:

    root_dir = Path(input("Please Enter the target folder you want to organize: "))

    if root_dir.exists():
        break

    print("Invalid Path. Please enter the full path of a valid folder on your machine.")

closet_dir = root_dir / 'closet'
closet_dir.mkdir(exist_ok = True)

text_dir = closet_dir / 'text_files'
text_dir.mkdir(exist_ok = True)

csv_dir = closet_dir / 'csv_files'
csv_dir.mkdir(exist_ok = True)

folders_dir = closet_dir / 'folders'
folders_dir.mkdir(exist_ok = True)

for item in root_dir.iterdir():
    if item == closet_dir:
        continue
    elif item.is_file() and item.suffix == '.txt':
        shutil.move(item, text_dir / item.name)
    elif item.is_file() and item.suffix == '.csv':
        shutil.move(item, csv_dir / item.name)
    elif item.is_dir() and 'temp' in item.name:
        shutil.rmtree(item)
    elif item.is_dir():
        shutil.move(item, folders_dir / item.name)
    else:
        shutil.move(item, closet_dir / item.name)


print("Success Folder clean-up complete!")






