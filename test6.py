friend = {
    'first_name': '博闻',
    'last_name': '唐',
    'age': 22,
    'city': 'jiangsu',
    }
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['city'])
print('--------')
favorite_numbers = {
    'a': 11,
    'b': 22,
    'c': 33,
    'd': 44,
    'e': 55,
    }

num = {favorite_numbers['a']}
print(f"a's favorite number is {num}.")

num = {favorite_numbers['b']}
print(f"b's favorite number is {num}.")

num = {favorite_numbers['c']}
print(f"c's favorite number is {num}.")

num = {favorite_numbers['d']}
print(f"d's favorite number is {num}.")

num = {favorite_numbers['e']}
print(f"e's favorite number is {num}.")
print('--------')
glossary = {
    'string': 'A series of characters',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items. one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    }

word = 'string'
print(f"{word.title()}: {glossary[word]}")
word = 'comment'
print(f"{word.title()}: {glossary[word]}")
word = 'list'
print(f"{word.title()}: {glossary[word]}")
word = 'loop'
print(f"{word.title()}: {glossary[word]}")
word = 'dictionary'
print(f"{word.title()}: {glossary[word]}")
print('--------')
glossary = {
    'string': 'A series of characters',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items. one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")
print('--------')

rivers = {
 'nile': 'egypt',
 'mississippi': 'united states',
 'fraser': 'canada',
 'kuskokwim': 'alaska',
 'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"-{river}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"-{country}")
print('--------')
people = []

person = {
    'first_name': '唐',
    'last_name': '博闻',
    'age': 22,
    'city': 'jiangsu',
}
people.append(person)

person = {
    'first_name': '廖',
    'last_name': '骞',
    'age': 22,
    'city': 'sichuan',
}
people.append(person)

person = {
    'first_name': '单',
    'last_name': '凯',
    'age': 23,
    'city': 'dongbei',
}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f"{name}, of {city}, is {age} years old.")

print('--------')
pets = []
pet = {
    'animal type': 'python',
    'name': 'john',
    'owener': 'guido',
    'weight': 43,
    'eats': 'bugs',
    }
pets.append(pet)
pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owener': 'eric',
    'weight': 37,
    'eats': 'shoes',
    }
pets.append(pet)
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
print('--------')
favorite_places = {
    'leo': ['the Himalayas', 'Mongolia', 'Spain'],
    'soris': ['hawaii', 'iceland'],
    'jack': ['Germany', 'Switzerland', 'Mexico'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
print('--------')
favorite_numbers = {
    'leo': [42, 17],
    'soris': [42, 39, 56],
    'jack': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f" {number}")
print('--------')
cites = {
    'santiago': {
        'country': 'chile',
        'population': 6310000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975453,
        'nearby mountains': 'himilaya',
        }
}
for city, city_info in cites.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()
    print(f"\n{city.title()} is in {country}.")
    print(f"\tIt has a population of about {population}.")
    print(f"\tThe {mountains} mounats are nearby.")

