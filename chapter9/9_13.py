"""
        骰子 创建一个Die类，它包含一个名为sides的属
    性，该属性的默认值为6。编写一个名为roll_die()的方法，它打
    印位于1和骰子面数之间的随机数。创建一个6面的骰子再掷10次。
    创建一个10面的骰子和一个20面的骰子，再分别掷10次。
"""
from random import randint


class Die:
    """一个表示骰子的类。"""

    def __init__(self, sides=6):
        """初始化骰子。"""
        self.sides = sides

    def roll_die(self):
        """返回一个位于 1 和骰子面数之间的随机数。"""
        return randint(1, self.sides)


d6 = Die()
results = []

for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("6 面的骰子掷 10 次")
print(results)

d10 = Die(sides=10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 面的骰子掷 10 次:")
print(results)

d20 = Die(sides=20)
results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n20 面的骰子掷 10 次")
print(results)
