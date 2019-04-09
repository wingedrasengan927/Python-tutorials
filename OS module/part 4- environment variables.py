

import os

os.chdir(r'C:\Users\neera\Desktop')

# let's say we want to access the onedrive directory location by grabbing the ONEDRIVE environment variable

# get only the path of onedrive environment variable
print(os.environ.get("ONEDRIVE"))

# Let's say we want to create a new file called 'test.txt' in the path that the environment variable gave us (i.e in the onedrive directory)
# For that, we need to join the two paths together (like 'C:\Users\neera\OneDrive'+'\test.txt')
# for that, we're gonna use the os.path module

# Let's join the two paths
# the join method takes in multiple arguments which are the paths to be joined
file_path = os.path.join(os.environ.get("ONEDRIVE"), 'text.txt')
print(file_path)

print("\n")


with open(file_path, "w") as f:
    f.write("hey")

# let's see if that file is created
print(os.listdir(os.environ.get("ONEDRIVE"))) # It's been created

print("\n")

# check the directory name
print(os.path.dirname(file_path))

# check the basename
print(os.path.basename(file_path))

# get both directory name and basename
print(os.path.split(file_path))

# check whether a given path exists
print(os.path.exists(file_path))  # returns True

# check whether something is a directory
print(os.path.isdir(file_path)) # returns false

# check whether something is a file
print(os.path.isfile(file_path)) # returns true

# split the root of the path and the extension
# first one is the file name without the extension
# second one is the extension of that file
print(os.path.splitext(file_path))