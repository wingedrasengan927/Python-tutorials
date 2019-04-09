
# let's see how to look at some information about our files
# like size of the file, last modification time etc

import os

os.chdir(r'C:\Users\neera\Desktop')
print(os.stat('test.txt')) # gives all the information about the file

# let's see modified time in a readable format
from datetime import datetime
modified_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(modified_time))

print("\n")

# Now Let's say we want to see the entire directory tree and the files within

# os.walk is a generator that yields three tuples
# 1. Directory Path 2. Directories within the path 3. Files within the path
# by default, it traverses from top down

for dirpath, dirnames, filenames in os.walk(r'C:\Users\neera\Desktop'):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files", filenames)
    print()

# So, what does it do
# It started in the desktop as our current path
# and then it printed out all the directories within the desktop
# and all of the files in within the desktop
# and now it goes down to each of the directories one at a time
# and prints out the directories and files within the directory
# the process is repeated till it goes down the entire tree

