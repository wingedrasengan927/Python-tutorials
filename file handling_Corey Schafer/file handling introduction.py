# File Objects

# To get the file object, we can use the built in 'open' command
# A file called 'dummy.txt' is created in the same directory for reference purpose
# If the file is not in the same directory, you have to pass the file path into the open command

# The open command allows us to specify whether we want to read, write, append the file

# read - 'r'
# write - 'w'
# read and write - 'r+'

f = open('dummy.txt', 'r')

# print the name of the file
print(f.name)

# to check the mode of file ()
print(f.mode)

# we need to explicitly close the file after opening it
f.close()

