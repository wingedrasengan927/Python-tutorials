# ---------READING AND WRITING FILES----------
# 1.the great thing about reading and writing files is that we can
#   store data for future use

import os

# 1.lets start the code with 'with'
#   it is going to guarantee that the file closes if the program crashes
# 2.mode='w' means we want to overwrite the file ( if you don't put anything
#   the default is going to be read )
# encoding='utf-8' means we write in unicode(ascii 2) language
# 3.we store the data in myFile
# 4.write functions allows us to write the file

with open("mydata.txt", mode='w', encoding="utf-8") as myFile:
    myFile.write("Some random shit\nMore random shit\nsome more random shit")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())  # reads every line of the file as a single string

print(myFile.closed)  # returns true if the file is closed
print(myFile.name)  # returns the name of the file
print(myFile.mode)  # returns the mode

# some methods of os module

os.rename("mydata.txt", "mydata2.txt")  # renames the file
os.remove("mydata2.txt")  # removes the file
#  os.mkdir("mydir")  # creates a directory
os.chdir("mydir")  # allows us to change into the new directory, we have created

print("Current Directory: ", os.getcwd())  # returns the current directory

# lets delete the directory
# first move into the below directory ( pycharm projects ) in this case

os.chdir("..")  # moves a step back
print("Current Directory: ", os.getcwd())  # returns the current directory
os.rmdir("mydir")  # removes the directory

import os

# read file one line at a time

with open("mydata.txt", mode='w', encoding="utf-8") as myFile:
    myFile.write("Some random shit\nMore random shit\nsome more random shit")

with open("mydata.txt", encoding="utf-8") as myFile:
    # to track what line is being read
    lineNum = 1
    while True:

        line = myFile.readline() # this is going to read one line at a time
        # if not line means that line has no data to read
        if not line:
            break

        print("Line", lineNum, ": ", line, end="")

        lineNum += 1

# Problem
# in each line of the file
# output the number of words
# output the average word length

import os

with open("mydata.txt", mode='w', encoding='utf-8') as myFile:
    myFile.write("Hey What's Up\nNothing much bro\nThen fuck off")

with open("mydata.txt", encoding="utf-8") as myFile:
    sum = 0
    lineNum = 1
    while True:
        line = myFile.readline()
        if not line:
            break

        line = line.lower()

        count = 0
        for i in line:
            if i.isalnum():
                count += 1

        print("line", lineNum, ":", "Number of words = ", count)
        lineNum += 1
        sum = sum + count

print("The average number of words are: ", sum/(lineNum-1))

# --------TUPLES---------

# a tuple is just like a list but it's values cannot be changed

myTuple = (1, 2, 3, 4, 5, 6)

print(myTuple[0])  # returns the first value
print(myTuple[0:3])  # returns the range upto 3
print(len(myTuple))  # returns the length of tuple

# tuple concatenation

myTuple = myTuple + (7, 8, 9, 10)
print(myTuple)

# to check if a particular value is in tuple

print("is 10 in mytuple? ", 10 in myTuple)

# iterate through the tuple
for i in myTuple:
    print(i)

# convert list into tuple
aList = [1, 3, 7]
aTuple = tuple(aList)
print(aTuple)
aList = list(aTuple)
print(aList)

# string typecasting
count = 45
count = str(count)
print(type(count))

# get min and max values of tuple
print(min(aTuple))
print(max(aTuple))