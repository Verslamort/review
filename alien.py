alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x'] = 0
alien_0['y'] = 25
print(alien_0)

print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
print('--------')

alien_1 = {'x': 0, 'y': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x']}")
# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快。
    x_increment = 3
alien_1['x'] = alien_1['x'] + x_increment
print(f'New position: {alien_1["x"]}')
print('--------')
del alien_0['points']
print(alien_0)
