"""
    调查 编写一个while循环，询问用户为何喜欢编程。
    每当用户输入一个原因后，都将其添加到一个存储所有原因的文件
    中。
"""
filename = 'text_files/reason.txt'
while True:
    problem = input('请回答，您为何喜欢编程？')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(problem)
