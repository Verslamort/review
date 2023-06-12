"""
    城市和国家 编写一个函数，它接受两个形参：一个城
    市名和一个国家名。这个函数返回一个格式为City, Country的字
    符串，如Santiago, Chile。将这个函数存储在一个名为
    city_functions.py的模块中。
    创建一个名为test_cities.py的程序，对刚才编写的函数进行测试
    （别忘了，需要导入模块unittest和要测试的函数）。编写一个
    名为test_city_country()的方法，核实使用类似
    于'santiago'和'chile'这样的值来调用前述函数时，得到的字
    符串是正确的。运行test_cities.py，确认测试
    test_city_country()通过了。

    人口数量 修改前面的函数，加上第三个必不可少的形
    参population，并返回一个格式为City, Country –
    population xxx的字符串，如Santiago, Chile – population
    5000000。运行test_cities.py，确认测试test_city_country()未
    通过。
    修改上述函数，将形参population设置为可选的。再次运行
    test_cities.py，确认测试test_city_country()又通过了。
    再编写一个名为test_city_country_population()的测试，核
    实可以使用类似
    于'santiago'、'chile'和'population=5000000'这样的值来
    调用这个函数。再次运行test_cities.py，确认测试
    test_city_country_population()通过了。
"""


def get_city_country(city, country, population=''):
    """返回格式为City, Country的字符串"""
    if population:
        city_country = (city + ', ' + country).title() + ' - ' + population
    else:
        city_country = (city + ', ' + country).title()
    return city_country
