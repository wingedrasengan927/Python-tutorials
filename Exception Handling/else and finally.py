
# else runs the code that needs to be executed if the try doesn't throw an error

# finally block runs no matter what happens
# whether the code is successful or it throws an error, the finally block runs

a = 1
b = 2
try:
    c = a+b
except ValueError as e:
    print(e)
else:
    print(c)
finally:
    print("Exit")