class Employee:
    def __init__(self, first_name=str, last_name=str, pay=int):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def raise_pay(self, raise_amount):
        self.pay += raise_amount

if __name__ == "__main__":
    neeraj = Employee("Neeraj", "Krishna", 50000)
    print(neeraj.email)
    print(neeraj.full_name)