# -----Special Methods or Magic Methods------

# They help us to emulate some built-in behaviour in python
# And this is how we can perform operator overloading
# by defining our own special methods, we'll be able to change some of the built-in behaviour and operations

# these special methods are always surrounded by '__'
# these double underscores are also called dunder

# in general, when we print an object, like print(emp_1)
# it gives a vague output
# Let's solve this in this video

class Employee:

    raise_percent = 1.05

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = self.firstname + "." + self.lastname + "@company.com"

    def apply_raise(self):
        self.pay = self.pay * self.raise_percent

    def fullname(self):
        return  self.firstname + self.lastname

    # let's take a look at some more special methods

    # In short, repr is meant to be an unambigous representation of an object
    # and should be used for debugging, logging and things like that
    # good rule of thumb while creating this method
    # is to try to display something that you can copy and paste back in the python code
    # that would re-create that same object
    # for example, something like 'Employee()'

    def __repr__(self):
        # so, here we are trying to return a string that can be used to re-create an object
        return "Employee('{}', '{}', {})".format(self.firstname, self.lastname, self.pay)


    # In short, str is meant to be a readable representation of an object
    # and is meant to be used as a display for the user

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # Let's look at few more special methods

    # Let's create our 'addition'
    # so by adding two employees, we can sum their salary
    # self will be on the left side of the addition
    # other will be on the right side
    def __add__(self, other):
        return self.pay + other.pay

    # we can define our own 'len' method for our employee class
    # Let's say it will return the total number of characters in employee's fullname
    def __len__(self):
        return len(self.fullname())



emp_1 = Employee("Neeraj", "Krishna", 123000)
emp_2 = Employee("Corey", "Scafer", 200000)

# Let's see the special Methods in action
# Now if I normally try to print an object, it gives a vague output
# But since I've used the special Method repr
# You can see it gives a different output
# So, this is what special methods do
# they change the built-in behaviour
print(emp_1) # Employee(Neeraj, Krishna, 123000)

# Now, if we use try to print our employee object
# after defining the str method
# It'll use that instead of repr method
print(emp_1) # NeerajKrishna - Neeraj.Krishna@company.com

# Now we can still access repr and str specifically
print(repr(emp_1))
print(str(emp_2))

# This is what is happening in the background
print(emp_1.__repr__())
print(emp_2.__str__())

# So, using these special methods,
# we've been able to change how the objects are displayed

# Let's say we do this
print(1+2) # 3
# In the background, It's using a special method called __add__
# we can access this from the integer object
print(int.__add__(1, 2)) # 3

# strings have their own __add__ method
print(str.__add__("a", "b"))

# So, Now we can customize how this __add__ method acts for our objects by creating that method
# like by adding two employees, we can sum their total salary
# Let's try it out
print(Employee.__add__(emp_1, emp_2))
# or
print(emp_1 + emp_2) # return the sum of salary's
# see, we've created our addition!

# the 'len' method is also a special method
print(len("test")) # 4
# or
print(str.__len__("test")) # 4
# or
print("test".__len__()) # 4

# Let's see our len method in action
print(len(emp_1))

