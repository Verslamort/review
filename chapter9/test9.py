"""
    餐馆 创建一个名为Restaurant的类，为其方法
    __init__()设置属性restaurant_name和cuisine_type。创建
    一个名为describe_restaurant()的方法和一个名
    为open_restaurant()的方法，前者打印前述两项信息，而后者
    打印一条消息，指出餐馆正在营业。
    根据这个类创建一个名为restaurant的实例，分别打印其两个属
    性，再调用前述两个方法。
    三家餐馆 根据为完成练习9-1而编写的类创建三个实
    例，并对每个实例调用方法describe_restaurant()。

    就餐人数 在为完成练习9-1而编写的程序中，添加一个
    名为number_served的属性，并将其默认值设置为0。根据这个类
    创建一个名为restaurant的实例。打印有多少人在这家餐馆就餐
    过，然后修改这个值并再次打印它。
    添加一个名为set_number_served()的方法，让你能够设置就餐
    人数。调用这个方法并向它传递一个值，然后再次打印这个值。
    添加一个名为increment_number_served()的方法，让你能够将
    就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这
    家餐馆每天可能接待的就餐人数。
"""


# 1.创建类
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} is open."
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('麦当劳', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# ludvigs = Restaurant("肯德基", 'bread')
# ludvigs.describe_restaurant()
#
# mango_thai = Restaurant('华莱士', 'hamburg')
# mango_thai.describe_restaurant()


print(f"\n初始人数: {restaurant.number_served}")
restaurant.number_served = 430
print(f"更改初始人数: {restaurant.number_served}")

# 3
restaurant.set_number_served(1257)
print(f"设置就餐人数: {restaurant.number_served}")

# 4
restaurant.increment_number_served(239)
print(f"可能接待的就餐人数: {restaurant.number_served}")

"""
    用户 创建一个名为User的类，其中包含属
    性first_name和last_name，以及用户简介通常会存储的其他几
    个属性。在类User中定义一个名为describe_user()的方法，用
    于打印用户信息摘要。再定义一个名为greet_user()的方法，用
    于向用户发出个性化的问候。
    创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
    
    尝试登录次数 在为完成练习9-3而编写的User类中，添
    加一个名为login_attempts的属性。编写一个名
    为increment_login_attempts()的方法，将属
    性login_attempts的值加1。再编写一个名
    为reset_login_attempts()的方法，将属性login_attempts的
    值重置为0。
    根据User类创建一个实例，再调用方法
    increment_login_attempts()多次。打印属性login_attempts
    的值，确认它被正确地递增。然后，调用方法
    reset_login_attempts()，并再次打印属性login_attempts的
    值，确认它被重置为0。
"""


class User:

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户（姓，名，用户名，电子邮箱，地址）"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息摘要。"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """问候用户"""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        """次数清零"""
        self.login_attempts = 0


leo = User('廖', '骞', 'Leo', '1571188577@qq.com', 'sichuan')
leo.describe_user()
leo.greet_user()

jack = User('jack', 'willian', 'ass', '20020920@163.com', 'California')
jack.describe_user()
jack.greet_user()

leo.increment_login_attempts()
leo.increment_login_attempts()
leo.increment_login_attempts()
print(f"登录尝试次数: {leo.login_attempts}")


leo.reset_login_attempts()
print(f"登录尝试次数: {leo.login_attempts}")
