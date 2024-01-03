tree_map = []
routes = [[1, 1],[3, 1],[5, 1],[7, 1],[1, 2]]

with open('input.txt') as input_file:
    for line in input_file:
        tree_map.append(line.rstrip())

tree_map_as_lists = []

# convert each line in the map into a list of characters
for line in tree_map:
    line_as_list = []
    for ch in line:
        line_as_list.append(ch)
    tree_map_as_lists.append(line_as_list)

tree_counts = []

# try each route
for route in routes:
    
    #reset the variable for each route attempt
    map_x_pos = 0
    tree_count = 0
    map_line_num = 0

    # define which map lines are relevant, based on the defined slope for the route
    map_lines_to_check = []
    for value in range(len(tree_map)):
        if map_line_num <= len(tree_map) - 1:
            map_lines_to_check.append(map_line_num)
            map_line_num += route[1]
        else:
            break
    
    # build the new map based on map_lines_to_check
    new_map = []
    for line in map_lines_to_check:
        new_map.append(tree_map_as_lists[line])
        

    # count the trees on each route
    for map_line in new_map:

        if map_x_pos > len(map_line) -1:
            map_x_pos -= len(map_line)
        test_pos = map_line[map_x_pos]
        if test_pos == '#':
            tree_count += 1
            #print(map_line_num)

        map_x_pos += route[0]

    print(f"you hit {tree_count} trees")
    tree_counts.append(tree_count)

    answer = 1

    for x in tree_counts:
        answer = answer * x
    
print(f"the answer is {answer}")