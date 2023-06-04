pizzas = ['蔬菜', '水果', '拼盘']
for pizza in pizzas:
    print(pizza)
    print(f'I like {pizza} pizza.')
print('I really love pizza!')
print('--------')
animals = ['cat', 'dog', 'pig']
for animal in animals:
    print(f'A {animal} would make a great pet.')
print('They all have four legs.')


cubes = [cube**3 for cube in range(1, 11)]
print('The first three items in the list are:')
print(cubes[:3])
print('Three items from the middle of the list are:')
print(cubes[3:6])
cubes = [cube**3 for cube in range(1, 11)]
print('The last three items in the list are:')
print(cubes[-3:])
