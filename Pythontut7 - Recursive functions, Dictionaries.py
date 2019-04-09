# ---------------DICTIONARIES----------------
# dictionaries instead of following a sequential order like lists, follow a key and value system
# we access a value by it's key

neerajDict = {"name":"Neeraj Krishna", "age": 20, "Policy":"Fuck Everything"}
print(neerajDict["name"])
print(neerajDict["age"])
neerajDict["city"] = "Warangal"
print("is there a city", "city" in neerajDict)  # returns true
print(neerajDict.values())  # returns all the values in a dictionary
print(neerajDict.keys())  # returns all the keys in a dictionary
print(neerajDict.items())  # returns the value, key pair
# iterating using a for loop
for v, k in neerajDict.items():
    print(v, ":", k)

# another way to get the value
print(neerajDict.get("mname", "not here"))  # if "mname" is not there, it returns the default
                                            # "not here" in this case

# delete a key value
del neerajDict["Policy"]
print(neerajDict)  # deletes policy

# deletes all the data in the dictionary
neerajDict.clear()
print(neerajDict)  # returns nothing

# create lists that are able to hold dictionaries

employees = []
while True:
    try:
        fname, lname = input("Enter your first name and last name: ").split()
        break
    except:
        print("Error! Please Enter both your first name and last name")
        continue

# appending a dictionary to a list
employees.append({"first name":fname, "last name": lname})
print(employees)

# Problem
# Create a customer list
# like this

# Enter Customer (Yes/No) : yes
# Enter Customer name : Zelda
# Enter Customer (Yes/No) : yes
# Enter Customer name : Mario
# Enter Customer (Yes/No) : no
# zelda
# mario

customerList = []

while True:
    yes_no = input("Enter Customer (Yes/No) :")
    yes_no = yes_no.lower()
    if yes_no == "yes":
        name = input("Enter Customer name :")
        name = name.lower()
        customerList.append(name)
    elif yes_no == "no":
        print("The Customers are: ")
        print()
        for i in customerList:
            print(i)
    else:
        print("Error! Please enter either 'yes' or 'no'")


# -----------RECURSIVE FUNCTIONS--------------

# a function that returns itself

# make a factorial function


def factorial(a):
    # condition
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)


print(factorial(3))

# problem
# calculate fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13  (third number = sum of 1st two numbers)


def fibonacciseq(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        result = fibonacciseq(num - 1) + fibonacciseq(num - 2)
        return result


sequence  = []
lastnumber = int(input("enter the range: "))
for i in range(1, lastnumber + 1):
    sequence.append(fibonacciseq(i))

print("The sequence is: ")
for k in sequence:
    print(k, end=", ")