"""
    彩票分析 可以使用一个循环来明白前述彩票大奖有多
    难中奖。为此，创建一个名为my_ticket的列表或元组，再编写一
    个循环，不断地随机选择数或字母，直到中大奖为止。请打印一条
    消息，报告执行循环多少次才中了大奖。
"""
from random import choice


def get_winning_ticket(possibilities):
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket


def check_ticket(win_tickets, tickets):
    n = 0
    my_tickets = []
    while True:
        i = 0
        copy_tickets = tickets[:]
        while i < len(win_tickets):
            n += 1
            chioce = choice(copy_tickets)
            my_tickets.append(chioce)
            copy_tickets.remove(chioce)
            i += 1
        if my_tickets != win_tickets:
            while my_tickets:
                my_tickets.pop()
            continue
        else:
            print(f'您抽的号码为：\n{my_tickets}')
            print('\n恭喜你中奖了')
            print(f'您抽奖抽了{n}次')
            break


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
win = get_winning_ticket(numbers)
print(f'本期开奖号码：\n{win}')
check_ticket(win, numbers)

