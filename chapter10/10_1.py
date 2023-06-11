"""
    Python学习笔记 在文本编辑器中新建一个文件，写几
    句话来总结一下你至此学到的Python知识，其中每一行都以“In
    Python you can”打头。将这个文件命名为learning_python.txt，并存
    储到为完成本章练习而编写的程序所在的目录中。编写一个程序，
    它读取这个文件，并将你所写的内容打印三次：第一次打印时读取
    整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储
    在一个列表中，再在with代码块外打印它们。

    读取你刚创建的文件learning_python.txt中的每一行，将其中的
    Python都替换为另一门语言的名称，比如C。将修改后的各行都打
    印到屏幕上。
"""
# 第一次打印
with open('text_files/python.txt') as f:
    print(f.read())

# 第二次打印
with open('text_files/python.txt') as f:
    for line in f:
        print(line.rstrip())

# 第三次打印
with open('text_files/python.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# 替换
with open('text_files/python.txt') as f:
    contents = f.read()
    print(contents.replace('Python', 'C'))
