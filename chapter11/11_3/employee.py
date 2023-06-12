"""
    雇员 编写一个名为Employee的类，其方法
    __init__()接受名、姓和年薪，并将它们存储在属性中。编写一
    个名为give_raise()的方法，它默认将年薪增加5000美元，但也
    能够接受其他的年薪增加量。
    为Employee编写一个测试用例，其中包含两个测试方
    法：test_give_default_raise()和
    test_give_custom_raise()。使用方法setUp()，以免在每个测
    试方法中都新建雇员实例。运行这个测试用例，确认两个测试都通
    过了。
"""


class Employee:
    def __init__(self, first_name, last_name, annul_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annul_salary = annul_salary

    def give_raise(self, add_annul_salary=5000):
        self.annul_salary = self.annul_salary + add_annul_salary

