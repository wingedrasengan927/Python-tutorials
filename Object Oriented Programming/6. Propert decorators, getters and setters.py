# -------PROPERTY DECORATOR---------

# This allows to get our class attribute's getter, setter and deleter functionality

# The property decorator allows us to define a method but we can access the method like an attribute
# Let's go and pull this email attribute out into a method similar to our fullname method

# Setter's
# Let's add a property decorator to fullname method similar to the email method
# but, in this case, Let's say we want to change the fullname
# and doing so should also change the firstname, lastname and email
# so, if do emp_1.fullname = Corey Schafer
# Then the changes should be:
# firstname = Corey
# lastname = Schafer
# email = Corey.Schafer@company.com

# Deleter's
# Let's say I want to delete an employee


class employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def email(self):
        return "{}.{}@company.com".format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    # Let's define a setter
    # The name of the setter should be name of the property
    # 'fullname' in this case

    @fullname.setter
    def fullname(self, name):
    # Name is the value we are trying to set. e.g., 'Corey Schafer'
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.firstname = None
        self.lastname = None


emp_1 = employee("Neeraj", "Krishna")

print(emp_1.firstname)
print(emp_1.lastname)
print(emp_1.fullname)
print(emp_1.email)

# Now, Let's change the first name
emp_1.firstname = "Jim"

print(emp_1.firstname) # Jim
print(emp_1.lastname) # Krishna
print(emp_1.fullname) # Jim Krishna
print(emp_1.email) # Neeraj.Krishna@company.com

# As we can see
# the fullname changes and the email doesn't change
# The reason is the fullname method grabs the CURRENT firstname and lastname

# we have to fix the email
# This is where getters and setters come in
# We can do this in python using property decorator

# Now we can see, adding property decorator solves the problem
# Now, the email method can be accessed as an attribute
print(emp_1.email)

# Now, let's try out our setter
emp_1.fullname = "Corey Schafer"
print(emp_1.firstname) # Corey
print(emp_1.lastname) # Schafer
print(emp_1.email) # Corey.Schafer@company.com

# What happened is, when we set emp_1.fullname = "Corey Schafer"
# It went directly to our setter method and carried out the process

# So the deleter runs when we delete an attribute
del emp_1.fullname

