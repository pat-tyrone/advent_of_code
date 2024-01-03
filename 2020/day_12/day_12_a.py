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
heading = 90

for step in dir_pairs:
    print(f"\ndirection: {step}")
    travel_dir = ''

    if step[0] in ['R', 'L']:
        heading = heading + (step[1] * turns[step[0]])
        while heading >= 360:
            heading = heading - 360
        while heading < 0:
            heading = heading + 360
    
    elif step[0] in ['N', 'S', 'E', 'W']:
        travel_dir = step[0]
    elif step[0] == 'F':
        travel_dir = headings[heading]
    else:
        print("SOMETHING WENT WRONG")

    if travel_dir == 'N':
        y = y + step[1]
    elif travel_dir == 'S':
        y = y - step[1]
    elif travel_dir == 'E':
        x = x + step[1]
    elif travel_dir == 'W':
        x = x - step[1]
    
    # print(f"new location: x={x}, y={y}")
    # print(f"heading: {heading}")

    print(f"part 1 answer = {abs(x) + abs(y)}")



