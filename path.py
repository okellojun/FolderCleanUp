#Converting file path strings into path objects
# Add r before the path
from pathlib import Path

#p = r'/home/reborntechke/Desktop/py/file_clean_up_project'

p = input("Please Enter the target folder: ")

path = Path(p)

if path.exists():
    print('I exist!!')