import random
import math
# ------------------LISTS------------
# lists can be heterogeneous, they may contain different types of data

randlist = ["ahfdusj", 12.24, 567]

oneToten = list(range(10))

# list concatenation
randlist = randlist + oneToten

# get the length of the string
print(len(randlist))

# list slicing

for i in randlist[0:3]:
    print("{} : {}".format(randlist.index(i), i))

# print item multiple times (multiplication)
print(randlist[0] * 3)

# to find out whether our particular string or any other variable is in the list
print("ahfdusj" in randlist)

# to find out how many times a variable is present in a list
print(randlist.count("ahfdusj"))

# put another item at the very end of the list
randlist.append(12)

# generate list of random values between 1 and 9
list1 = []
for i in range(5):
    list1.append(random.randrange(1, 9))

print(list1)

# bubble sort
# way to sort a list

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop
# completes one cycle.
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. check if list[index] > list[index+1]
# 5. If so swap the index values
# 6. When the inner loop completes, the largest number is at the end of the list
# 7. Decrement the outer loop by 1


# lets create a number list
numlist = []

for i in range(10):
    numlist.append(random.randrange(0, 20))

i = len(numlist) - 1

while i > 1:
    j = 0
    while j < i:

        print("\nis {} > {}".format(numlist[j], numlist[j+1]))

        if numlist[j] > numlist[j+1]:
            print("Switch")
            temp = numlist[j]
            numlist[j] = numlist[j + 1]
            numlist[j+1] = temp
        else:
            print("Don't Switch")
        j += 1

        for k in numlist:
            print(k, end=", ")
        print()

    print("END OF ROUND")
    i -= 1

for i in numlist:
    print(i, end=", ")

print()

# ---------EASIER BUBBLE SORT ALGORITHM (MY VERSION)--------

# declaring the list
list111 = []
for i in range(10):
    list111.append(random. randrange(51))
print("Before sorting")
print(list111)

# bubble sort

# outer loop
for j in range(len(list111)-1):
    # inner loop
    for i in range(len(list111) - 1):
        if list111[i] > list111[i + 1]:
            temp = list111[i + 1]
            list111[i + 1] = list111[i]
            list111[i] = temp

print("after sorting")
print(list111)

# -----------------------------------------------------

# Some other list functions

import random
numlist2 = []

for i in range(10):
    numlist2.append(random.randrange(0,10))

numlist2.sort()  # sorts the listr
numlist2.reverse()  # reverses the list
numlist2.insert(10, 25)  # stores 25 in the 10th index
numlist2.remove(25)  # removes 25 ( the value stored inside the list )
numlist2.pop(2)  # removes value stored at index 2, returns only 9 items

print(numlist2)

import math

# list comprehensions are just another way to construct a list
# they allow us to perform operations on every value of list
# lets create an evenlist

evenlist = [i*2 for i in range(10)]  # i iterates through the range and is multiplied by 2
print(evenlist)

# if we want to perform multiple operations on the elements of list
# creates a list of lists

# creates a two dimensional list (list in lists)
numList = [1, 2, 3, 4, 5]
listofPowers = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]  # for m in numlist, perform the operations in the square brackets

print(listofPowers)

# create a multi dimensional list

multiDlist = [[0]*10 for i in range(10)]  # it means that we want to have a list of 10 zeros for every
# value of i as i iterates through the range

print(multiDlist)


# Problem
# Generate a multiplication table like this

'''
1, 2, 3, 4, 5, 6,  7, 8, 9
2, 4, 6, 8, 10, 12, 14, 16 ,18
......
......
'''
# use a multidimensional list

# ------ USING LIST COMPREHENSIONS-------
# nested list comprehensions

list100 = list(range(1, 11))
x = int(input("Enter upto which number you want the tables: "))
j = 1
listx = [[i*j for i in list100] for j in range(1, x+1)]
for i in listx:
    print(i)


# If you try to access the
# empty or None element by pointing available index of list,
# Then you will get the List index out of range error.

