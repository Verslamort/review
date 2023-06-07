# 消息 编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print('function')


display_message()


# 喜欢的图书 编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个函数打印一条消息，下面是一个例子。
# One of my favorite books is Alice in Wonderland.
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book():
    title = 'The Catcher in the rvu'
    print(f'One of my favorite books is {title}.')


favorite_book()
"""
T恤 编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
"""


def make_shirt(size, sample):
    print(f'The shirt size is {size} and type is {sample}')


make_shirt("M", "YYDS")
"""
    大号T恤 修改函数make_shirt()，使其在默认情况下
    制作一件印有“I love Python”字样的大号T恤。调用这个函数来制
    作：一件印有默认字样的大号T恤，一件印有默认字样的中号T
    恤，以及一件印有其他字样的T恤（尺码无关紧要）。
"""


def make_shirt(size1='L', sample1='I love Python'):
    print(f'The shirt size is {size1} and type is {sample1}')


make_shirt()
make_shirt(size1='M')
make_shirt(sample1='Middle')
"""
    城市 编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单
    的句子，下面是一个例子。
    Reykjavik is in Iceland.
    给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
"""


def describe_city(city, country='Japan'):
    print(f'{city} is in {country}')


describe_city(city='Tokyo')
describe_city(city='NewYork', country='Amercia')
describe_city(city='Osaka')


# 城市名 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。


def city_country(city, country):
    all = f'{city},{country}'
    return all.title()


print(city_country('tokyo', 'japan'))
print(city_country('santiago', 'chile'))
c1 = city_country('beijing', 'china')
print(c1)
"""
    专辑 编写一个名为make_album()的函数，它创建一个
    描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返
    回一个包含这两项信息的字典。使用这个函数创建三个表示不同专
    辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的
    信息。
    给函数make_album()添加一个默认值为None的可选形参，以便存
    储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将该
    值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中
    指定专辑包含的歌曲数。
"""


def make_album(singer, album, song=""):
    # 它创建一个描述音乐专辑的字典
    album1 = {
        'singer': singer, 'album': album,
    }
    if song:
        # 放进album1列表中
        album1['song'] = song
    return album1


while True:
    singer = input('please input singer:')
    album = input('please input album:')
    # 创建的字典印出来
    album2 = {singer, album}
    print(album2)
    problem = input('Do u want to quit?')
    if problem == 'Y':
        break

a1 = make_album('Taylor', '22', '22')
a2 = make_album('kesha', 'This is me')
a3 = make_album('Avicii', 'TIM')
print(a1)
print(a2)
print(a3)
"""
    消息 创建一个列表，其中包含一系列简短的文本消
    息。将该列表传递给一个名为show_messages()的函数，这个函
    数会打印列表中的每条文本消息。
    发送消息 在你为完成练习8-9而编写的程序中，编写
    一个名为send_messages()的函数，将每条消息都打印出来并移
    到一个名为sent_messages的列表中。调用函
    数send_messages()，再将两个列表都打印出来，确认正确地移
    动了消息。
    消息归档 修改你为完成练习8-10而编写的程序，在调
    用函数send_messages()时，向它传递消息列表的副本。调用函
    数send_messages()后，将两个列表都打印出来，确认保留了原
    始列表中的消息。
"""


def show_messages(show_msg):
    for msg in show_msg:
        print(msg)


def send_messages(show_msg, send_msg):
    while show_msg:
        current_msg = show_msg.pop()
        print(f'Sent_messages:{current_msg}')
        send_msg.append(current_msg)


show_msg = ['abc', 'cba', 'nba']
send_msg = []

show_messages(show_msg)
send_messages(show_msg[:], send_msg)
