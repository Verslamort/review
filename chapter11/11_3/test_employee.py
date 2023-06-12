import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        first_name = 'albert'
        last_name = 'einstein'
        annul_salary = 10000
        self.my_employee = Employee(first_name, last_name, annul_salary)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annul_salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(20000)
        self.assertEqual(self.my_employee.annul_salary, 30000)


if __name__ == '__main__':
    unittest.main()
