p1_data = []
with open('d3_data.txt') as f:
    for line in f:
        p1_data.append(line.rstrip())


def get_activators(number, address):
    above_addresses = [(address[0] - 1, address[1] - 1), (address[0] - 1, address[1])]
    below_addresses = [(address[0] + 1, address[1] - 1), (address[0] + 1, address[1])]
    left_address = [(address[0], address[1] - 1)]
    right_address = [(address[0], address[1] + len(number))]

    for i in range(len(number)):
        above_addresses.append((address[0] - 1, address[1] + i + 1))
        below_addresses.append((address[0] + 1, address[1] + i + 1))
    
    return above_addresses + below_addresses + left_address + right_address

# for part 1
activator_map = []
for line in p1_data:
    map_row = []
    for i, v in enumerate(line):
        if not v.isdigit() and v != '.':
            is_activator = True
        else:
            is_activator = False
        map_row.append(is_activator)
    activator_map.append(map_row)

# for part 2
gear_map = []
for line in p1_data:
    map_row = []
    for i, v in enumerate(line):
        if v == '*':
            is_gear = True
        else:
            is_gear = False
        map_row.append(is_gear)
    gear_map.append(map_row)

# for both parts
number_addresses = {}
line_num = 0
for line in p1_data:
    number_string = ''
    for i, v in enumerate(line):
        if v.isdigit():
            number_string = number_string + v
            if len(number_string) == 1:
                idx = i
            if i == len(line) - 1:
                number_addresses[(line_num, idx)] = number_string
        elif number_string != '':
            number_addresses[(line_num, idx)] = number_string
            number_string = ''
    line_num += 1

p1_answer = 0
p2_answer = 0
gears_dict = {}

for k, v in number_addresses.items():
    number_activated = False
    for poss_act in get_activators(v, k):
        try:
            is_activator = activator_map[poss_act[0]][poss_act[1]]
            if is_activator:
                number_activated = True

            is_gear = gear_map[poss_act[0]][poss_act[1]]
            if is_gear:
                try:
                    gears_dict[(poss_act)].append(k)
                except:
                    gears_dict[(poss_act)] = [k]
            
        except:
            pass
    
    if number_activated:
        p1_answer += int(v)

# for part 2
for gear, numbers in gears_dict.items():
    if len(numbers) == 2:
        gear_product = int(number_addresses[numbers[0]]) * int(number_addresses[numbers[1]])
        p2_answer += gear_product

print(p1_answer)
print(p2_answer)