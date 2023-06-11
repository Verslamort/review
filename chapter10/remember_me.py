# 保存和读取用户生成的数据
# 存储用户名字
import json


username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
print(f"We'll remember you when you come back, {username}!")
