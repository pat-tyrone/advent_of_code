import re

directions = []

# imports the seat map
with open('input') as input_file:
    for line in input_file:
        directions.append(line.rstrip())

dir_pairs = []


for direction in directions:
    action = re.match("[a-z]", direction, re.IGNORECASE)
    action = action.group()
    action_len = len(action)

    num = int(direction[action_len:])
    
    dir_pair = (action, num)
    dir_pairs.append(dir_pair)


headings = {0: 'N' , 90: 'E' , 180: 'S' , 270: 'W'}
turns = {'R': 1, 'L': -1}

x = 0
y = 0

wp_x = 10
wp_y = 1

for step in dir_pairs:

    # # strictly for debugging:
    # print(f"\nstarting loc: x={x}, y ={y}")
    # print(f"direction: {step}")
    
    travel_dir = ''

    if step[0] in ['R', 'L']:
        new_wp = [0,0]
        if step[1] == 90:
            new_wp[0] = wp_y * turns[step[0]]
            new_wp[1] = wp_x * -1 * turns[step[0]]
        elif step[1] == 180:
            new_wp[0] = wp_x * -1
            new_wp[1] = wp_y * -1
        elif step[1] == 270:
            new_wp[0] = wp_y * -1 * turns[step[0]]
            new_wp[1] = wp_x * turns[step[0]]
        
        wp_x = new_wp[0]
        wp_y = new_wp[1]
    

    elif step[0] == 'N':
        wp_y = wp_y + step[1]
    elif step[0] == 'S':
        wp_y = wp_y - step[1]
    elif step[0] == 'E':
        wp_x = wp_x + step[1]
    elif step[0] == 'W':
        wp_x = wp_x - step[1]

    elif step[0] == 'F':
        x = x + (wp_x * step[1])
        y = y + (wp_y * step[1])
    
    # # strictly for debugging:
    # print(f"new location: x={x}, y={y}")
    # print(f"new waypoint: wp_x={wp_x}, wp_y={wp_y}")
    

print(f"part 2 answer = {abs(x) + abs(y)}")



