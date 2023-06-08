# # 存储所点比萨的信息。
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
# # 概述所点的比萨。
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print(topping)
#
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
#     }
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")


# 传递任意数量实参
# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    # """打印顾客点的所有配料。"""
    # print(toppings)
    """概述要制作的比萨。"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

