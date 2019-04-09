# The OS module allows us to interact with the underlying operating system in several different ways.
#  - Navigate the file system
#  - Get file information
#  - Look up and change the environment variables
#  - Move files around - Many more To begin,
#
# import the os module.
import os
# This is a built in module, no third party modules need to be installed.

# Something useful when working with a new module.
print(dir(os))
# This will show all the attributes and methods we have access to in this module

# Print out the current working directory
print(os.getcwd())

# Navigate to other directory
# Let's navigate to desktop
os.chdir(r'C:\Users\neera\Desktop') # Change Directory to Desktop

print(os.getcwd()) # Directory changed to desktop

# Let's list all the files and folders present in the current directory
# by default, the path is current working directory
print(os.listdir())

# Let's create a folder on desktop with name 'OS-Demo'

# there are two methods to do this

# 1
os.mkdir("OS-Demo-1") # make directory
# 2
# recommended method
os.makedirs("OS-Demo-2/Sub-Dir") # this method allows you to go many levels deep into the directory

# Let's delete the folders

# It's similar to make directory
# two methods

#1
# preferred method.
os.rmdir("OS-Demo-1") # remove directory
#2
# You have to specify the levels also. Otherwise, It'll show error.
os.removedirs("OS-Demo-2/Sub-Dir")