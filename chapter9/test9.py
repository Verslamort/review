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

    冰激凌小店 冰激凌小店是一种特殊的餐馆。编写一个
    名为IceCreamStand的类，让它继承为完成练习9-1或练习9-4而编
    写的Restaurant类。这两个版本的Restaurant类都可以，挑选你
    更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个
    由各种口味的冰激凌组成的列表。编写一个显示这些冰激凌的方
    法。创建一个IceCreamStand实例，并调用这个方法。

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


class IceCreamStand(Restaurant):
    """一个表示冰激凌小店的类。"""

    def __init__(self, name, cuisine_type='ice_cream'):
        """初始化冰激凌小店。"""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """显示出售的冰激凌品种。"""
        print("\n我们有以下几种口味:")
        for flavor in self.flavors:
            print(f"- {flavor}")


big_one = IceCreamStand('冰激凌小店', '怪味冰激凌')
big_one.flavors = ['甜', '酸', '苦', '辣']
big_one.describe_restaurant()
big_one.show_flavors()


# ludvigs = Restaurant("肯德基", 'bread')
# ludvigs.describe_restaurant()
#
# mango_thai = Restaurant('华莱士', 'hamburg')
# mango_thai.describe_restaurant()


# print(f"\n初始人数: {restaurant.number_served}")
# restaurant.number_served = 430
# print(f"更改初始人数: {restaurant.number_served}")
#
# # 3
# restaurant.set_number_served(1257)
# print(f"设置就餐人数: {restaurant.number_served}")
#
# # 4
# restaurant.increment_number_served(239)
# print(f"可能接待的就餐人数: {restaurant.number_served}")

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
    
    管理员 管理员是一种特殊的用户。编写一个名为Admin
    的类，让它继承为完成练习9-3或练习9-5而编写的User类。添加一
    个名为privileges的属性，用于存储一个由字符串（如"can add
    post"、"can delete post"、"can ban user"等）组成的列
    表。编写一个名为show_privileges()的方法，显示管理员的权
    限。创建一个Admin实例，并调用这个方法。
    
    权限 编写一个名为Privileges的类，它只有一个属
    性privileges，其中存储了练习9-7所述的字符串列表。将方法
    show_privileges()移到这个类中。在Admin类中，将一
    个Privileges实例用作其属性。创建一个Admin实例，并使用方
    法show_privileges()来显示其权限。

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


class Admin(User):
    """有管理权限的用户。"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员。"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


class Privileges:
    """一个存储管理员权限的类。"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- 此用户没有权限")


# leo = User('廖', '骞', 'Leo', '1571188577@qq.com', 'sichuan')
# leo.describe_user()
# leo.greet_user()
#
# jack = User('jack', 'willian', 'ass', '20020920@163.com', 'California')
# jack.describe_user()
# jack.greet_user()
#
# leo.increment_login_attempts()
# leo.increment_login_attempts()
# leo.increment_login_attempts()
# print(f"登录尝试次数: {leo.login_attempts}")
#
#
# leo.reset_login_attempts()
# print(f"登录尝试次数: {leo.login_attempts}")


eric = Admin('廖', '骞', 'Leo', '1571188577@qq.com', 'sichuan')
eric.privileges.show_privileges()
eric.describe_user()

print('\n正在添加权限......')
eric_privileges = ['can add post', 'can delete post', 'can ban user']
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
