"""
    电瓶升级 在本节最后一个electric_car.py版本中，给
    Battery类添加一个名为upgrade_battery()的方法。该方法检查
    电瓶容量，如果不是100，就将其设置为100。创建一辆电瓶容量为
    默认值的电动汽车，调用方法get_range()，然后对电瓶进行升
    级，并再次调用get_range()。你将看到这辆汽车的续航里程增加
    了。
"""


class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """电动汽车没有油箱。"""
        print("This car doesn't have a gas tank!")


# 重写父类方法

class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程。"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 85:
            range = 315

        message = f"这辆车可以行驶 {range}"
        message += " 满负荷行驶"
        print(message)

    def upgrade_battery(self):
        """在可能的情况下将电瓶升级。"""
        if self.battery_size == 75:
            self.battery_size = 85
            print("将电池升级到 85.")
        else:
            print("电池已经升级")


class ElectricCar(Car):
    """电动汽车的独特之处。"""
    def __init__(self, manufacturer, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
        print("制作一辆电动车并检查电池")


my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()

print("\n升级电池并再次检查:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

print("\n尝试第二次升级电池.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

