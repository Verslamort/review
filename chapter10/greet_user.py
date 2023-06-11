# 问候已存储名字的用户
import json


filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
print(f"Welcome back, {username}!")
