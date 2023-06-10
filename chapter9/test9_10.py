"""
    导入Restaurant类 将最新的Restaurant类存储在一
    个模块中。在另一个文件中，导入Restaurant类，创建一
    个Restaurant实例并调用Restaurant的一个方法，以确认
    import语句正确无误。
"""
from chapter9.test9 import Restaurant


channel_club = Restaurant('麦当劳', 'pizza')
channel_club.describe_restaurant()
channel_club.open_restaurant()
