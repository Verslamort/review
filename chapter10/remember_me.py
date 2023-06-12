"""
    验证用户 最后一个remember_me.py版本假设用户要
    么已输入用户名，要么是首次运行该程序。我们应该修改这个程
    序，以防当前用户并非上次运行该程序的用户。
    为此，在greet_user()中打印欢迎用户回来的消息前，询问他用
    户名是否正确。如果不对，就调用get_new_username()让用户输
    入正确的用户名。
"""
# 保存和读取用户生成的数据
# 存储用户名字
import json


def get_stored_username():
    """如果存储了用户名，就获取它。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """问候用户，并指出其名字。"""
    username = get_stored_username()
    print(f'您的用户名是否为：{username}？')
    user = input('正确请输入Y，错误请输入N：')
    if user == 'Y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"您的正确用户名是：{username}!")


greet_user()
