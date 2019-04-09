# -----------STRING FUNCTIONS---------

rand_string = "    this is a very important string "

print(rand_string.lstrip())  # removes the whitespace at the left side
print(rand_string.rstrip())  # removes the whitespace at the right side
print(rand_string.strip())  # removes the whitespace at the left and the right side

rand_string = rand_string.strip()

print(rand_string.capitalize())  # capitalizes the first letter

print(rand_string.upper())  # prints every character in uppercase
print(rand_string.lower())  # prints every character in lowercase

# convert list into string ( joining all elements of a list )

a_list = ["bunch", "of", "random", "shit"]
print(" ".join(a_list))  # at the beginning, we specify how we want separate the elements(space in this case)

# convert string to list

a_list_2 = rand_string.split()

# iterating through the elements of list
for i in a_list_2:
    print(i)

# print how many "is" are there in our random string

print(rand_string.count("is"))

# find the index of the required string
# we will find the index of "important" in our random string
# it will return the index of the first character ( "i" in this case )

print(rand_string.find("important"))

# replace one substring with another substring

print(rand_string.replace("a very", "super"))

# Acronym Generator
# if the user enters random access memory, it should return RAM

Inp_String = input("Enter the String: ")
Out_String = Inp_String.upper()
Out_list = Out_String.split()
New_Out_String = ""
for i in Out_list:
    New_Out_String += i[0]

print("The acronym is: ", New_Out_String, sep="")

letter_z = "z"
number_3 = "3"
space = " "

# to know the data type present in the string

# is letter_z contains letters or numbers or both
print(letter_z.isalnum())  # returns true

# is letter_z contains only letter ( returns false if numbers or spaces are present )
print(letter_z.isalpha())  # returns true

# is number_3 contains only numbers
# doesn't work for floats
print(number_3.isdigit())  # returns true

# is letter_z lowercase or uppercase
print(letter_z.islower())  # returns true
print(letter_z.isupper())  # returns false

# is space contains only whitespace
print(space.isspace())  # returns true

# modify the function, so that it returns true for a float data type
float_Number = "3.3544"
# is Float_Number a float
print(float_Number.isdigit())  # returns false

# how to rectify that
# let us create a isfloat function


def isFloat(str_Val):
    try:
        float(str_Val)
        return True
    except ValueError:
        return False


print("is float_Number a float: ", isFloat(float_Number))  # returns true for int also

# Problem: Make a cipher
# each letter is shifted bt 3 spaces ( A becomes D and B becomes E )

# A - Z 65 - 90
# a - z 97 - 122

# some rules to be followed
# Do not change the numbers or whitespace or symbols, leave them as they are


# Solution
inp_String = input("Enter the code that you want to encode: ")
key = int(input("Enter the key: "))
out_String = ""

for i in inp_String:
    thor = ord(i)
    if i.isupper():
        if (thor + key) > ord("Z"):
            thor = (thor + key) - 26
        else:
            thor = thor + key
    elif i.islower():
        if (thor + key) > ord("z"):
            thor = (thor + key) - 26
        else:
            thor = thor + key
    out_String += str(chr(int(thor)))

print("The Encrypted message is: ", out_String)

# decrypting\

new_out_String = ""
for i in out_String:
    thor = ord(i)
    if i.isupper():
        if (thor - key) < ord("A"):
            thor = thor - key + 26
        else:
            thor = thor - key
    elif i.islower():
        if (thor - key) < ord("a"):
            thor = thor - key + 26
        else:
            thor = thor - key
    new_out_String += str(chr(int(thor)))

print("The decrypted message is: ", new_out_String)