# ----------------FUNCTIONS---------------
# syntax of the function


def add_numbers(num1, num2):
    return num1 + num2


# local variable
# any variable defined in that function is available to only that function

# global variable
# any variable created outside the function


def change_name(name):
    name = "Mark"


name = "Tom"
change_name(name)
print(name)

# we can see that the value of global variable is not changed
# to change the name, we can use return


def change_name_new(name):
    return "Mark"


print(change_name_new(name))  # we can see that the value of name has been changed

# another way to do it
gbl_name = "Sammy"


def change_name_1():
    global gbl_name  # using global gives us the permission to change the global variable
    gbl_name = "Tony"


change_name_1()
print(gbl_name)  # the value has been changed


# Problem
# Solve for x
# users input will be like : x + 23 = 34
# rules:
# x should always be first
# only addition for now


def x_sol(equation):
    list1 = equation.split()
    result = int(list1[4]) - int(list1[2])
    resultinstring = str(result)
    print("x = " + resultinstring)


x_sol("x + 23 = 45")

# return multiple values


def multi_divide(num1, num2):
    try:
        return (num1 * num2), (num1/num2)
    except:
        num2 = 1
        return (num1 * num2), (num1/num2)


mult, div = multi_divide(10, 0)
print("10 * 0 = {}, 10/0 = {}".format(mult, div))

# return a list of primes
# a prime can be divided by one and itself

# create a function which checks for prime


def isPrime(num1):
    for i in range(2,num1):
        if num1 % i == 0:
            return False

    return True


def getPrimelist(maxnum):
    listprime = [1]
    for i in range(2,maxnum):
        if isPrime(i):
            listprime.append(i)

    return listprime


maxnum = int(input("Search for primes upto: "))
print("the list of primes upto {} are {}".format(maxnum, getPrimelist(maxnum)))

# deal with unknown number of arguments in the function


def sumofall(*args): # splat operator
    sum = 0
    for i in args:
        sum += i

    return sum


print("Sum: ", sumofall(1, 2, 3, 4, 5, 67))


