sandwich_orders = ['Francesinha', 'Cachopo', 'Mollete']
finished_sandwiches = []
while sandwich_orders:
    sandwich_orders1 = sandwich_orders.pop()
    print(f'I made your {sandwich_orders1} sandwich')
    finished_sandwiches.append(sandwich_orders1)
for so in finished_sandwiches:
    print(f'{so} is finish!')
print('--------')
sandwich_orders = ['pastrami', 'Francesinha', 'pastrami', 'Cachopo', 'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('Pastrami is sold out!')
print(sandwich_orders)
print('--------')
responses = {}
while True:
    name = input("What is your name?")
    response = input('If you could visit one place in the world, where would you go?')
    responses[name] = response
    repeat = input('Would you like to let another person respond?(yes/no)')
    if response == 'no':
        break
    for name, response in responses.items():
        print(f'{name} want to go {response}.')

