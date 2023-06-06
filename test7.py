car = input('What car would you want to find?')
print(f'Let me see if I can find you a {car}.')
print('--------')
answer = input('How many people would come to eat?')
answer = int(answer)
if answer > 8:
    print('Sorry')
else:
    print('Welcome,your seat is here')
print('--------')
num = input('Please input number:')
if num % 10 == 0:
    print('yes')
else:
    print('no')
print('--------')
prompt = 'Enter u want to use the batching:'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)
print('--------')
prompt = 'How old are u'
while True:
    age = input(prompt)
    if age < 3:
        print('free')
    elif age >= 3 and age <=12:
        print('$10')
    else:
        print('$15')
        break
print('--------')
prompt = 'Enter u want to use the batching'
active = input(prompt)
while True:
    if active == 'quit':
        break
    else:
        print(active)
print('--------')
while True:
    print('good')

