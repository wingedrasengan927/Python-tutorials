
# don't set default values to firstname, lastname etc. it creates lot of problems
# you never want to pass mutable datatypes such as a list or dictionary as empty arguments

# inheritance allows us to inherit attributes and methods from a parent class
# with this, we can create sub-classes and get all of the functionality of our parent class
# and we can add new functionality without affecting our parent class in any way

# let's say we want to create different sub-classes
# lets say we want to create developers and managers
# now both of them will have name and salary which we will inherit from the Employee class


class Employee:

    no_of_Employees = 0
    raise_percent = 1.05

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname= lastname
        self.pay = pay
        self.email = firstname + "." + lastname + "@company.com"
        Employee.no_of_Employees += 1

    def fullname(self):
        return self.firstname + self.lastname

    def apply_raise(self):
        self.pay = self.pay * self.raise_percent

    @classmethod
    def from_strings(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

# let's create developer sub-class
# in the parenthesis, we put the class we want to inherit from
# lets change the raise_percent in our developer sub class

# sometimes we want to initiate our sub classes with more information than our parent class
# lets say we also add their main programming language as an attribute
# to do this, we again have to use the init method, with small changes
# to initiate, instead of copying the code from the Employee class, what we can do is
# use super().__init__() and then pass in the common arguments. It lets the parent class handle the arguments


class Developer(Employee):

    raise_percent = 1.10

    def __init__(self, firstname, lastname, pay, prog_lang):
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang


# lets create another sub-class called manager

class Manager(Employee):
    raise_percent = 1.07

    def __init__(self, firstname, lastname, pay, employees = None):
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # add or remove a list of employees our manager supervises
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # method to print all the employees this manager supervises
    def employee_list(self):
        for emp in self.employees:
            print("-->", emp.fullname())




emp_1 = Employee.from_strings("Neeraj-Krishna-170000")
print(emp_1.email)
emp_2 = Employee("corey", "schaffer", 200000)

emp_3 = Developer("Bharadwaj", "Palakurthy", 230000, "Java")
print(emp_3.email)  # it works
# so what happened is, when we first Instantiated our developers, it looked in the developer
# class for the __init__ method, and when it did'nt find anything, python then
# walks up the chain of inheritance till it finds what it is looking for
# this chain is called the method resolution order

# help method helps to clearly visualize what's going on
print(help(Developer))

print(emp_3.pay)
emp_3.apply_raise()
print(emp_3.pay)
print(emp_1.raise_percent)
print(emp_3.raise_percent)
# The thing to take away from here is by changing the raise_percent in the Developers sub class
# will not have any effect on the Employee instances

# lets create our manager
man_1 = Manager("Preetham", "Ministries", 120000, [emp_1])
print(man_1.email)
print(man_1.employee_list())
man_1.add_employee(emp_2)
man_1.add_employee(emp_3)
man_1.remove_employee(emp_1)
print(man_1.employee_list())

# python has these built-in methods called
# isinstance: tells us if an object is an instance of the class
# issubclass: tells us if a class is subclass of another

print(isinstance(man_1, Manager))  # True
print(isinstance(man_1, Employee))  # True
print(isinstance(man_1, Developer))  # False

print(issubclass(Manager, Employee))  # True
print(issubclass(Developer, Employee))  # True
print(issubclass(Manager, Developer))  # True

