"""
    彩票 创建一个列表或元组，其中包含10个数和5个字
    母。从这个列表或元组中随机选择4个数或字母，并打印一条消
    息，指出只要彩票上是这4个数或字母，就中大奖了。
"""
from random import choice


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_num = []
print("开始抽号")


while len(winning_num) < 4:
    pulled_item = choice(possibilities)
    if pulled_item not in winning_num:
        print(f"你选择了 {pulled_item}!")
        winning_num.append(pulled_item)

print("\n你的彩票是...")
print(winning_num)
print("恭喜你中奖！")
