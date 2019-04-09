
# regular methods in a class automatically take the instance as an argument
# class methods automatically take the class as the first argument
# to convert regular methods to class methods, add decorator @classmethod
# that decorator alters the functionality of the method so that we recieve class as our first argument
# the common convention for class variables is cls, like 'self' is for instances

# class methods provide multiple ways or alternative constructors to create an object

# Let's look at static methods
# static methods, unlike class methods and regular methods don't pass anything automatically
# they behave like regular functions but we include them in the class because
# they have some logical connection to the class
# a method is a static method if you don't access the instance or the class anywhere within the function
# lets create a function that takes in a date and returns if it is a workday or not
# to create a static method, add decorator @staticmethod

class Employee:

    no_of_emps = 0
    raise_percent = 1.04

    def __init__(self, firstname="", lastname="", pay=0):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = self.firstname + "." + self.lastname + "@gmail.com"
        Employee.no_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = self.pay * self.raise_percent

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_percent = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # python has these weekday method
    # it returns 0 for monday and 6 for sunday and rest in between
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp_1 = Employee(firstname="Neeraj", lastname="Krishna", pay=170000)
emp_2 = Employee(firstname="John", lastname="Doe", pay=200000)

print(Employee.raise_percent)
print(emp_1.raise_percent)
print(emp_2.raise_percent)
# all of them output 1.04

# let's change the raise amount
Employee.set_raise_amt(1.05)  # this is the same as saying Employee.raise_amt = 1.05

print(Employee.raise_percent)
print(emp_1.raise_percent)
print(emp_2.raise_percent)
# all of them output 1.05

# let's say a person is entering their data in this format
emp_str_1 = 'Mark-Zuckerberg-100000000'
# let's create this instance from the employee class
first, last, pay = emp_str_1.split('-')
emp_3 = Employee(first, last, pay)
print(emp_3.firstname)  # it works!

# if this is a common case, we dont want them doing everything manually
# so, lets create an alternative constructor that allows them to pass the string
# and we can create an employee from the string

# let's check our new class method
emp_str_2 = "Bill-Gates-2000000"
emp_4 = Employee.from_string(emp_str_2)
print(emp_4.email)  # it works!

import datetime
my_date = datetime.date(2018, 8, 12)

# let's check our static method
print(Employee.is_workday(my_date)) # it fookin works!