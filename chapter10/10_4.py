"""
    访客名单 编写一个while循环，提示用户输入名字。
    用户输入名字后，在屏幕上打印一句问候语，并将一条到访记录添
    加到文件guest_book.txt中。确保这个文件中的每条记录都独占一
    行。
"""
filename = 'text_files/guest.txt'
while True:
    name = input('请输入您的名字：')
    # msg = print(f'欢迎{name}访问\n')
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(name)
        f.close()
