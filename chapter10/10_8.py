"""
    猫和狗 创建文件cats.txt和dogs.txt，在第一个文件中至
    少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编
    写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这
    些代码放在一个try-except代码块中，以便在文件不存在时捕获
    FileNotFound错误，并显示一条友好的消息。将任意一个文件移
    到另一个地方，并确认except代码块中的代码将正确执行。

    静默的猫和狗 修改你在练习10-8中编写的except代码
    块，让程序在任意文件不存在时静默失败。
"""
filenames = ['cats.txt', 'dogs.txt']
for i in filenames:
    try:
        with open(i, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        # print('文件不存在')
        pass
    