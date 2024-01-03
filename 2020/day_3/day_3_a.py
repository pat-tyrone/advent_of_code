tree_map = []

with open('input.txt') as input_file:
    for line in input_file:
        tree_map.append(line.rstrip())

tree_map_lists = []

# convert each line in the map into a list of characters
for line in tree_map:
    line_as_list = []
    for ch in line:
        line_as_list.append(ch)
    tree_map_lists.append(line_as_list)

map_x_pos = 0
tree_count = 0
counter = 1

for map_line in tree_map_lists:
    if map_x_pos > len(map_line) -1:
        map_x_pos += len(map_line) * -1
    test_pos = map_line[map_x_pos]
    if test_pos == '#':
        tree_count += 1
        #print(counter)

    map_x_pos += 3
    counter += 1


print(f"you hit {tree_count} trees")