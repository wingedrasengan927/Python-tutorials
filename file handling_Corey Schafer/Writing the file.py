
# Let's create a new file called dummy2
# If the file doesn't exist, It will create a new file
# If the file does exist, It will overwrite it
# If you don't want to overwrite the file, use 'a' for appending the file
with open('dummy2.txt', 'w') as f:
    f.write('testing...')
    # If we write another statement
    # It's going to pick up where we left, just like the read method
    f.write('1, 2, 3')

with open('dummy2.txt', 'w') as f:
    f.write('test')
    # you can use seek to set the position at the beginning of the file
    f.seek(0)
    f.write('R') # Output: Rest. because write method doesn't overwrite the file everytime
    # It doesn't delete the rest of the contents