
# printing odd numbers using for loop

for i in range(20):
    if i % 2 != 0:
        print(i)

# rounding off float type

your_float = input('Enter a floating point ')
your_float = float(your_float)
print("the value rounded off to two decimals is {:.2f}".format(your_float))


# Problem : Have user input their invest and expected interest each year
# After each year earning = investment + investment * interest
# print out the earning after 10 year period

investment, interest, No_of_Years = input('Enter the amount invested, the interest'+
                                          ' expected, time period ').split()
investment = float(investment)
interest = float(interest) * .01
No_of_Years = int(No_of_Years)

for i in range(No_of_Years):
    earning = investment + investment*interest

print('the earning after {} years is {:.2f}'.format(No_of_Years, earning))

# imp* floating point calculations are only precise upto 16 digits


# Random Numbers

import random


for i in range(50):
    rand_Num = random.randrange(1, 51)
    print(rand_Num)

# continue jumps back again into the loop
# break jumps out of the loop


# print even numbers using while loop
i = 1
while i <= 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# Problem : Print out a pine tree taking number of rows as input

# how to print without a new line ; print("xyz",end="")
# how to print without space in between ; print("xyz", "abc", sep="")

rows = input('Enter the number of rows ')
rows = int(rows)
space = rows - 1
stars = 1
for i in range(rows):
    for j in range(space):
        print(" ", end=" ")
    for k in range(stars):
        print('*', end= " ")
    print('\n')
    space = space - 1
    stars = stars + 2


