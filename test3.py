guests = ['A', 'B', 'C']
for guest in guests:
    print(f'{guest}, I want to invite you to party.')
print('--------')
guests[1] = 'D'
for guest in guests:
    print(f'{guest}, I want to invite you to party.')
print('--------')
guests.insert(0, 'E')
guests.insert(2, 'F')
guests.append('G')
for guest in guests:
    print(f'{guest}, I want to invite you to party.')
print('--------')
print(guests)
for guest in guests[2:]:
    print(f"Sorry {guests.pop()}, I can't invite you to my party.")
for guest in guests:
    print(f'Hey {guest.title()}, remember to come to my party.')
del guests[0]
del guests[1]
print(guests)



