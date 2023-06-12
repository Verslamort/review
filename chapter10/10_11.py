"""
    喜欢的数 编写一个程序，提示用户输入喜欢的数，
    并使用json.dump()将这个数存储到文件中。再编写一个程序，从
    文件中读取这个值，并打印如下所示的消息。
    I know your favorite number! It's _____.

    记住喜欢的数 将练习10-11中的程序合二为一。如果
    存储了用户喜欢的数，就向用户显示它，否则提示用户输入喜欢的
    数并将其存储到文件中。运行这个程序两次，看看它能否像预期的
    那样工作。
"""
import json


filename = '10_11.json'
try:
    with open(filename) as f:
        num = json.load(f)

except FileNotFoundError:
    num = input('请输入喜欢的数：')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(num, f)
        print(f"We'll remember the number of {num}")
else:
    print(f"Here's your favorite number: {num}")
