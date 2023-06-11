"""
    访客 编写一个程序，提示用户输入名字。用户做出响
    应后，将其名字写入文件guest.txt中。
"""
filename = 'guest.txt'
name = input('请输入您的名字：')
with open(filename, 'w', encoding='utf-8') as f:
    print(f.write(name))
