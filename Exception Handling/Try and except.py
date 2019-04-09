
# Try and except blocks help us to anticipate the sections of code that might throw an error
# We can use try and except blocks to handle the errors
# be as specific as possible with the errors

# Put the specific ones at the top
# and the more general ones at the bottom


try:
    f = open('textfile.txt')
except FileNotFoundError:
    print('Sorry, the file doesn\'t exist') # put a backward slash before ' to include it in the string to be printed
# if we want to print the actual errors, instead of custom messages, do this
except Exception as e: # "Exception" finds a very broad category of errors
    print(e)


# So what's happening here
# When we try to run the code in the try block
# if it throws an exception
# Then it checks for the error in each of the except blocks
# if the same error is found, it runs that particular except block

# you can also raise your own exceptions

a = 1
b = 2

try:
    c = a + b
    if c != 2:
        raise Exception # we can manually raise a particular exception
except Exception:
    print("the code is correct.")

