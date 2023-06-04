name = 'Eric'
print(f'Hello {name}, would you like to learn some Python today?')

print(name.title())
print(name.upper())
print(name.lower())

print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')

famous_person = "--法海"
message = "大威天龙"
print(message, "\n\t", famous_person)

name = "\tEric Leo\n"
print("Unmodified:")
print(name)
print("\nUsing lstrip():")
print(name.lstrip())
print("\nUsing rstrip():")
print(name.rstrip())
print("\nUsing strip():")
print(name.strip())

print(2+6)
print(9-1)
print(2*4)
print(16/2)

num = 6
message = 'My favorite number is ' + str(num) + '.'
print(message)

Transportation = ['balanced vehicle', 'car', 'motorcycle']
message = f'I would like to own a {Transportation[0].title()}.'
print(message)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

cycles = []
cycles.append('honda')
cycles.append('yamaha')
cycles.append('suzuki')
print(cycles)
cycles.insert(0, 'ducati')
print(cycles)
del cycles[2]
print(cycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")
cars = ['audi', 'bmw', 'auto']
cars.remove('audi')
print(cars)

