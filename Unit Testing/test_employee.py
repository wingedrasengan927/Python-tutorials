import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # runs once at the start
        print("setUpClass")

    @classmethod
    def tearDownClass(cls): # runs once at the end
        print("tearDownClass")

    def setUp(self): # runs before every test
        self.emp1 = Employee("Neeraj", "Krishna", 50000)
        self.emp2 = Employee("Ashish", "Kumar", 120000)

    def tearDown(self): # runs after every test
        pass

    def test_email(self):

        self.assertEqual(self.emp1.email, "Neeraj.Krishna@company.com")
        self.assertEqual(self.emp2.email, "Ashish.Kumar@company.com")

        self.emp1.first_name = "Vamsi"
        self.emp2.first_name = "John"

        self.assertEqual(self.emp1.email, "Vamsi.Krishna@company.com")
        self.assertEqual(self.emp2.email, "John.Kumar@company.com")

    def test_full_name(self):

        self.assertEqual(self.emp1.full_name, "Neeraj Krishna")
        self.assertEqual(self.emp2.full_name, "Ashish Kumar")

        self.emp1.first_name = "Vamsi"
        self.emp2.first_name = "John"

        self.assertEqual(self.emp1.full_name, "Vamsi Krishna")
        self.assertEqual(self.emp2.full_name, "John Kumar")

    def test_raise_pay(self):

        self.assertEqual(self.emp1.pay, 50000)
        self.assertEqual(self.emp2.pay, 120000)

        self.emp1.raise_pay(10000)
        self.emp2.raise_pay(20000)

        self.assertEqual(self.emp1.pay, 60000)
        self.assertEqual(self.emp2.pay, 140000)

if __name__ == "__main__":
    unittest.main()