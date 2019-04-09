# Object Oriented Programming

# Classes
# They allow us to logically group our data and functions in a way that's
# easy to reuse and also easy to build upon if need be

# Method: A function that is associated with a class

# A class is like a blueprint for creating instances
# instance variables contain attributes that is unique to each instance
# An object is an instance of the class

# let's create an employee class
# __init__ method is like 'to initialize'
# the 'self' is the instance. It's the default argument whenever you create a method inside a class
# other arguments can be accepted after self
# the attributes name need not be same as the arguments name
# let's create a method in the class which gives the full name
# each method in the class automatically takes instance as the first argument

class employee:
    def __init__(self, firstname="", lastname="", pay=0):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + "." + lastname + "@company.com"

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

# the instance is passed automatically as an argument
emp_1 = employee(firstname="Neeraj", lastname="Krishna", pay=170000)

print(emp_1.email)

# the instance will  be passed automatically as an argument in the method
print(emp_1.fullname())

# we can also run these methods using the class itself
# but when we run it from a class, we have to pass the instance as an argument
# when we call method off an instance, it automatically passes the instance as an argument
# but when we call the method off a class, we need to pass the instance as the argument
# in the background, when we call emp_1.fullname(), it get's transformed to employee.fullname(emp_1)
print(employee.fullname(emp_1))