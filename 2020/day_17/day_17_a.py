map_0 = []

with open('input.txt') as input_file:
    for line in input_file:
        map_0.append(line.strip())

# dictionary to hold map of the pocket dimension
pock_dim = {}

# establish the [min,max] values for each access. To be tracked for grow_dim_map and count_neighbors
# structure: [x_min, x_max, y_min, y_max, z_min, z_max]
pock_dim_limits = [0,0,0,0,0,0]

# formula to make sure the initial coordinates are set s.t. middle node is close to (0,0,0)
row_num_ref = (len(map_0) / 2) - ((len(map_0) % 2) / 2)
col_num_ref = ((len(map_0[0]) / 2) - ((len(map_0[0]) % 2) / 2)) * -1

pock_dim_limits[3] = row_num_ref
pock_dim_limits[0] = col_num_ref




# populate the dictionary with {(x,y,z): map_value} pairs. z=0 to start since input is 2-dimensional
row_num = row_num_ref
for row in map_0:
    col_num = col_num_ref
    for char in row:
        pock_dim[(col_num, row_num, 0)] = char
        pock_dim_limits[1] = col_num
        col_num += 1
    
    pock_dim_limits[2] = row_num
    row_num -= 1


def grow_dim_map(dim_map, dim_limits):
    """add a layer of empty ('.') spaces on all sides of dim_map"""
    x_min = int(dim_limits[0])
    x_max = int(dim_limits[1])
    y_min = int(dim_limits[2])
    y_max = int(dim_limits[3])
    z_min = int(dim_limits[4])
    z_max = int(dim_limits[5])

    for x in [x_min - 1, x_max + 1]:
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                dim_map[(x,y,z)] = '.'
    x_min = x_min - 1
    x_max = x_max + 1

    for y in [y_min - 1, y_max + 1]:
        for z in range(z_min, z_max + 1):
            for x in range(x_min, x_max + 1):
                dim_map[(x,y,z)] = '.'
    y_min = y_min - 1
    y_max = y_max + 1

    for z in [z_min - 1, z_max + 1]:
        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                dim_map[(x,y,z)] = '.'
    z_min = z_min - 1
    z_max = z_max + 1

    dim_limits[0] = x_min
    dim_limits[1] = x_max
    dim_limits[2] = y_min
    dim_limits[3] = y_max
    dim_limits[4] = z_min
    dim_limits[5] = z_max



# for k,v in pock_dim.items():
#     print(f"{k}: {v}")

# print(pock_dim_limits)
# print(len(pock_dim))



def count_neighbors(address, dim_map):
    """looks at one address in a 3d space, and counts how many of the 26 neighbors have a "#"""
    offsets = [-1, 0, 1]
    nbr_count = 0
    for x_os in offsets:
        for y_os in offsets:
            for z_os in offsets:
                if (x_os, y_os, z_os) != (0,0,0):
                    nbr_address = (address[0] + x_os, address[1] + y_os, address[2] + z_os)
                    try:
                        nbr = dim_map[nbr_address]
                        if nbr == '#':
                            nbr_count += 1
                    except:
                        continue
    
    return nbr_count

# for x in range(int(pock_dim_limits[0]), int(pock_dim_limits[1]+1)):
#     for y in range(int(pock_dim_limits[2]), int(pock_dim_limits[3]+1)):
#         for z in range(int(pock_dim_limits[4]), int(pock_dim_limits[5]+1)):

#             print(pock_dim[(x,y,z)])
#             print(count_neighbors((x, y, z), pock_dim))


def evolve(dim_map, dim_limits):
    """function to advance from t=0 to t=1, based on the rules"""

    grow_dim_map(dim_map, pock_dim_limits)

    dim_map_changes = {}
    for address in dim_map.keys():
        nbr_count = count_neighbors(address, dim_map)
        if dim_map[address] == '#' and nbr_count not in [2,3]:
            dim_map_changes[address] = '.'
        if dim_map[address] == '.' and nbr_count == 3:
            dim_map_changes[address] = '#'
    
    for k,v in dim_map_changes.items():
        dim_map[k] = v

def count_active(dim_map):
    """count the number of active cubes in the dimension map"""
    active_count = 0
    for address in dim_map.keys():
        if dim_map[address] == '#':
            active_count += 1
    
    return active_count

# for k,v in pock_dim.items():
#     print(k,v)

# print("\n")

for value in range(6):
    evolve(pock_dim, pock_dim_limits)

# for k,v in pock_dim.items():
#     print(k,v)

print(count_active(pock_dim))


