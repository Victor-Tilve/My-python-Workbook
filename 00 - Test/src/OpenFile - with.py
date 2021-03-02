import os
#basepath = 'D:\03 - Python programs\00 - Tests\01 - Open files'
#basepath = 'D:\\03 - Python programs\\00 - Tests\\01 - Open files'
basepath = 'D:'

with os.scandir(basepath) as entries:
    for entry in entries:
        print(entry.name)