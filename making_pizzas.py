# 导入函数
# 使用as给模块指定别名  import pizza as p
# 导入模块中所有的函数 from pizza import *
from pizza import make_pizza  # as mp


make_pizza(16, 'pepperoni')  # mp(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
