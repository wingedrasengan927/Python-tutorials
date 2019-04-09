
# Instance variables are those which are set using the self argument
# like self.firstname, self.lastname
# Instance variables are unique to each instance

# Class variables are variables shared among all instances
# They are the same for each instance

# let's say we want to create a method which rises every employees pay by a particular percent
# now, the pay_rise is same for all employees
# but we've got to update it everytime
# We can do it manually everytime but that's not preferred
# that is where the class variables come in
# we define them in the class

# to access these class variables,
# we need to access them through the class itself or an instance of the class
# we can access them from the class itself or from an instance of the class

# ---go to the bottom and then come up--

# init method runs every time we create a new employee
# let's say we want to keep on track the number of employees


class Employee:

    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = self.firstname + self.lastname
        # it's better to use Employee.num_of_employees instead of self
        # since it has to be constant for all instances
        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.firstname + self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # or Employee.pay

emp_1 = Employee(firstname="Neeraj", lastname="krishna", pay=170000)
emp_2 = Employee(firstname="Corey", lastname="Scafer", pay=120000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# if these are class variables, then how can we access them from the instance?
# if we are trying to access an attribute of an instance,
# it first checks whether the instance contains that attribute, if it doesn't
# then it checks if the class it inherits from contains that attribute
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# let's check the namespace
print(emp_1.__dict__)  # there is no raise_amount attribute
print(Employee.__dict__)  # there is a raise_amount attribute
# Now, the instance accesses this raise_amount attribute from the class

# let's change the raise amount
Employee.raise_amount = 1.05
# as you can it changes the raise amount for the class as well as all the instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# let's change the raise amount from the instance
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# it changes the raise amount for only that particular instance
# when we said emp_1.raise_amount, it actually created the raise_amount attribute within emp_1
emp_1.raise_amount = 1.06
print(emp_1.__dict__)  # see, a raise_amount attribute has been created
# so, first it checks the attributes of the instance, if it finds them,
# it'll not be checking the class
# since, emp_2 instance has no such attribute, it'll be accessing the class' attribute
# however, if you use the apply_raise method for emp_1, if we use Employee.raise_amount in that method,
# there will be no change
# use self.raise_amount in the applyraise method to make sure that the method is applied
# when used from the emp_1 instance

print(Employee.num_of_employees)