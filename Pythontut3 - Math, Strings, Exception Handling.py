# Exception Handling
# let us ask the user to enter a number
# chances are they are not going to
# we may know the type of error in this case

while True:
    # we put the block of code that may have an error in the try block
    try:
        number = int(input("Please Enter a number: "))
        break
# once it detects an error, it checks the except blocks to find that particular type of error
# once the error is found, the code stops there
    except ValueError:
        print("this is a Value Error")
# if none of the except blocks contain the error, then we use a default block
    except:
        print("This is an Unknown Error")

print("thank you for entering the number")

# Problem: Create a guess the number game using a do while loop
# PS : Make your own do while loop

import random

while True:
    # generate a random number
    Rand_No = random.randrange(1, 11)
    # take input from the user
    try:
        number1 = int(input("Please Enter a number between 1 and 10: "))
        if number1 >= 1 and number1 <= 10:
            if number1 == Rand_No:
                print("Congratulations you have won!")
                a = input("press 1 to play again and 2 to quit")
                if a == "1":
                    continue
                elif a == "2":
                    break
                else:
                    print("please enter a valid number")
                    break
            else:
                print("Sorry, you have lost")
                a = input("press 1 to play again and 2 to quit ")
                if a == "1":
                    continue
                elif a == "2":
                    break
                else:
                    print("please enter a valid number")
                    break
        else:
            print("please enter a valid number")
            continue
    except ValueError:
        print("Please Enter a valid number")
        continue

print("Thank you for playing")

# ---------- MATH MODULE - ---------
# Python provides many functions with its Math module
import math

# Because you used import you access methods by referencing the module
print("ceil(4.4) = ", math.ceil(4.4))
print("floor(4.4) = ", math.floor(4.4))
print("fabs(-4.4) = ", math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4
print("factorial(4) = ", math.factorial(4))

# Return remainder of division
print("fmod(5,4) = ", math.fmod(5, 4))

# Receive a float and return an int
print("trunc(4.2) = ", math.trunc(4.2))

# Return x^y
print("pow(2,2) = ", math.pow(2, 2))

# Return the square root
print("sqrt(4) = ", math.sqrt(4))

# Special values
print("math.e = ", math.e)
print("math.pi = ", math.pi)

# Return e^x
print("exp(4) = ", math.exp(4))

# Return the natural logarithm e * e * e ~= 20 so log(20) tells
# you that e^3 ~= 20
print("log(20) = ", math.log(20))

# You can define the base and 10^3 = 1000
print("log(1000,10) = ", math.log(1000, 10))

# You can also use base 10 like this
print("log10(1000) = ", math.log10(1000))

# We have the following trig functions
# sin, cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# Convert radians to degrees and vice versa
print("degrees(1.5708) = ", math.degrees(1.5708))
print("radians(90) = ", math.radians(90))

# ---------- ACCURATE FLOATING POINT CALCULATIONS ----------

# The decimal module provides for more accurate floating point calculations
# With from you can reference methods without the need to reference the module
# like we had to do with math above
# We create an alias being D here to avoid conflicts with methods with the same name

from decimal import Decimal as D

sum = D(0)
sum += D("0.01")
sum += D("0.01")
sum += D("0.01")
sum -= D("0.03")

print("Sum = ", sum)

# --------- STRINGS -------------
# Single quote or double quote are the same while creating a string
# string stores each character in an array

sample_string = "this is a very important string"
print(sample_string[0])  # returns t
print(sample_string[-1])  # returns the last character

print("Length is: ", len(sample_string))  # returns the length of the string
print(sample_string[0:4])  # string slicing
print(sample_string[8:])  # slices from 8th index to end
print("What's" + " up")  # string concatenation
print("Hello " * 5)  # string multiplication (prints the string 5 times)

# string in pairs

for i in range(0, len(sample_string)-1, 2):  # we subtract -1 because the last index is 30 not 31
    print(sample_string[i] + sample_string[i+1])

num_to_convert = str(2432)  # String type casting

# iterate through each character in the string

for char in sample_string:
    print(char, end=" ")

# ASCII 2 codes
# A - Z 65 - 90
# a - z 97 - 122

print("\n")
print("code of A is", ord("A"))  # method to return the code of A
print("the character associated with 65 is ", chr(65))  # returns the character associated with code


# Problem
# User enters the string in uppercase, convert it into ascii codes and print the secret message

Inp_String = input("Enter the String in Upper Case: ")
Out_String = ""
for i in range(0, len(Inp_String)):
    Out_String += str(ord(Inp_String[i]))

print("the secret message is: ", Out_String)


# Problem
# User enters the string in ANYCASE, convert it into ascii codes and print the secret message
# convert it back to the original message

Inp_String = input("Enter the String: ")
Out_String = ""
for i in range(0, len(Inp_String)):
    Out_String += str(ord(Inp_String[i]))

print("the secret message is: ", Out_String)

New_Out_String = ""
for i in range(0, len(Out_String), 2):
    New_Out_String += str(chr(int(Out_String[i]+Out_String[i+1])))

print("The original message is: ", New_Out_String)


# another solution
# convert everything to two digits by subtracting 23
# the number 23 because it is the least number to be subtracted by which all codes become two digits
# 122(higest code) - 99(highest two digit number) = 23

Inp_String = input("Enter the String: ")
Out_String = ""
for i in Inp_String:
    Out_String += str(ord(i) - 23)

print("The secret message is: ", Out_String)

New_Out_String = ""
for i in range(0, len(Out_String)-1, 2):
    New_Out_String += str(chr(int(Out_String[i]+Out_String[i+1]) + 23))

print("The original message was", New_Out_String)

# also to convert a string which contains space add and subtract 33 instead of 23
# reason : the UTF code of " " is 32. If we subtract 23 from 32 we get 9. 9 has only 1 digit
# therefore we get an error later. If we subtract 33 from 32 we get -1 and -1 has two digits.
# Therefore the programme works again.﻿



