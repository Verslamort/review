car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


a = 'I want to walk'
b = 'I want to run'
print(a == b)
print(a != b)

c = 'Leo'
d = 'leo'
print(d == c.lower())
print(d == c)
print('--------')
o = 21
p = 9
print(o < 20)
print(o < 22)
print(o < 22 and p > 8)
print(o < 22 and p < 8)
print(o < 22 or p < 8)
print(o > 22 or p < 8)
print('--------')
U = [1, 2, 3, 4, 5]
Y = 4
print(Y in U)
print(Y not in U)
print('--------')
# 5_3
# alien_color = 'green'
# if alien_color == 'green':
#     print('you get 5 points')
# alien_color = 'yellow'
# if alien_color == 'green':
#     print('you get 5 points too')

# 5_4
# alien_color = 'red'
# if alien_color == 'yellow':
#     print('you get 5 points')
# else:
#     print('you get 10 points')

# 5_5
alien_color = 'yellow'
if alien_color == 'green':
    print('you get 5 points')
elif alien_color == 'yellow':
    print('you get 10 points')
else:
    print('you get 15 points')
print('--------')
age = 19
if age < 2:
    print('baby')
elif age < 4:
    print('infant')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('elder')
print('--------')
favorite_fruits = ['apple', 'bananas', 'orange', 'lemon', 'melon']
if 'apple' in favorite_fruits:
    print('You really like apple!')
if 'bananas' in favorite_fruits:
    print('You really like bananas!')
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'lemon' in favorite_fruits:
    print('You really like lemon!')
if 'melon' in favorite_fruits:
    print('You really like melon!')
print('--------')
users = ['admin', 'jack', 'join', 'mary', 'lisa']
for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user},thank you for logging in again.')
print('--------')
users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin')
        else:
            print(f'having user {user}')
else:
    print('We need to find some users')
print('--------')
current_users = ['llf', 'fq', 'wyf', 'chy', 'zqy']
# 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users 中。
new_users = ['lqq', 'mh', 'sxr', 'Llf', 'tlj']
for new_user in users:
    if new_user in current_users:
        print('please input other user')
    else:
        print('user is not be use')
current_users = ['LLF', 'fq', 'WYF', 'chy', 'mh']
new_users = ['llf', 'FQ', 'wyf', 'CHY', 'MH']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry,this name has been used')
    else:
        print('Succeed')
print('--------')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
