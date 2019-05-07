
# Let's open a file using a context manager

# the benefit of using a context manager is they allow us to work on the files within the block
# Once we exit the block of code, the file is automatically closed
# It also closes the file if any exceptions are thrown

with open('dummy.txt') as f:
    # Let's read the contents of our file
    f_contents = f.read()
    print(f_contents)

    # Let's say you have an extremely large file and you don't want to load all the contents into the memory
    # There are couple of other methods to read other than f.read()

    # we get a list of all the lines in the file
    # It gets every line of the file as a different element of the list
    print(f.readlines()) # returns empty list
    # reason being readlines() method only reads the unread lines
    # Every line has already been read in the start by using the read() method
    # so there's nothing to read
    # It picks up where it left off
    # hence the empty list

    # one line is considered the distance between the first character to the 'enter' character
    # So, sometimes readline may even read the entire paragraph because that's the definition of what a line is

    # grab the firstline
    print(f.readline()) # returns nothing. reason above.

print("\n")

with open('dummy.txt') as f:
    # To read a very big file, we could iterate over each line
    # this is efficient since it's not reading the contents of the file all at once
    # hence no memory issue
    for line in f:
        print(line, end='')

print("\n")

with open('dummy.txt') as f:
    # With read method, we can actually specify the amount of data to be read
    # this can be done by passing size as an argument
    # passing 100 means, first 100 characters will be printed

    # first 100
    print(f.read(100))

    # next 100
    print(f.read(100))

print("\n")

# So, how do we use these to read large files with these methods
# we're going to use some kind of loop
# that iterates over small chunks at a time

# reading large data
with open('dummy.txt', 'r') as f:

    size_of_chunk = 10
    f_contents  = f.read(size_of_chunk)

    # to track the position, we can use the tell method
    # if it returns 10, it means currently, we are at the 10th position
    print(f.tell())

    # We can manipulate the current position using the seek method
    f.seek(20) # As you can see the output doesn't contain characters 10-20

    while len(f_contents) > 0:
        print(f_contents,end='')
        f_contents = f.read(size_of_chunk)


print("\n")




