aoc_data = []
with open('data_10.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())

def define_s(map_lol):
    s = {}
    found_s = False
    for r_i, r in enumerate(map_lol):
        if found_s:
            break
        for c_i, c in enumerate(r):
            if c=='S':
                s['coords'] = (r_i, c_i)
                found_s = True
                break

    possible_s_shapes = ['|', '-', 'L', 'J', '7', 'F']
    impossible_s_shapes = []

    try:
        left = map_lol[s['coords'][0]][s['coords'][1] - 1]
        if left not in ['-', 'L', 'F']:
            impossible_s_shapes.extend(['-', 'J', '7'])
    except:
        impossible_s_shapes.extend(['-', 'J', '7'])

    try:
        right = map_lol[s['coords'][0]][s['coords'][1] + 1]
        if right not in ['-', '7', 'J']:
            impossible_s_shapes.extend(['-', 'L', 'F'])
    except:
        impossible_s_shapes.extend(['-', 'L', 'F'])

    try:
        above = map_lol[s['coords'][0] - 1][s['coords'][1]]
        if above not in ['|', '7', 'F']:
            impossible_s_shapes.extend(['|', 'L', 'J'])
    except:
        impossible_s_shapes.extend(['|', 'L', 'J'])

    try:
        below = map_lol[s['coords'][0] + 1][s['coords'][1]]
        if below not in ['|', 'L', 'J']:
            impossible_s_shapes.extend(['|', '7', 'F'])
    except:
        impossible_s_shapes.extend(['|', '7', 'F'])
    
    for shape in set(impossible_s_shapes):
        possible_s_shapes.remove(shape)
    
    assert len(possible_s_shapes) == 1

    s['shape'] = possible_s_shapes[0]

    return s

def first_cxns(map_lol):
    s_dict = define_s(map_lol)
    coord_val = s_dict['shape']
    r = s_dict['coords'][0]
    c = s_dict['coords'][1]

    neigbs = {
        '|': ((1,0),(-1,0)),
        '-': ((0,-1),(0,1)),
        'L': ((-1,0),(0,1)),
        'J': ((-1,0),(0,-1)),
        '7': ((0,-1),(1,0)),
        'F': ((0,1),(1,0))
    }

    # Relative Coordinates of connections (cxsns)
    rel_coords = neigbs[coord_val]

    cxns = [(r + rc[0], c + rc[1]) for rc in rel_coords]

    return cxns

def next_cxns(map_lol, coord, last_coord):
    """returns two coordinates that connect to the coord given"""
    # note that coord is (r, c), i.e. (y, x)

    r = coord[0]
    c = coord[1]
    coord_val = map_lol[r][c]

    neigbs = {
        '|': ((1,0),(-1,0)),
        '-': ((0,-1),(0,1)),
        'L': ((-1,0),(0,1)),
        'J': ((-1,0),(0,-1)),
        '7': ((0,-1),(1,0)),
        'F': ((0,1),(1,0))
    }

    # Relative Coordinates of connections (cxsns)
    rel_coords = neigbs[coord_val]

    cxns = [(r + rc[0], c + rc[1]) for rc in rel_coords]

    cxns.remove(last_coord)

    return cxns[0]


# loop_coords is only referenced in part 2, but populated as the algo walks over the hash map for part 1
loop_coords = []
for i in range(len(aoc_data)):
    lc_row = []
    for j in range(len(aoc_data[0])):
        lc_row.append('.')
    loop_coords.append(lc_row)

s_coords = define_s(aoc_data)['coords']
loop_coords[s_coords[0]][s_coords[1]] = 'x'

# set values according to S before starting while loop
lc = [s_coords, s_coords]
nc = first_cxns(aoc_data)

for cp in nc:
    loop_coords[cp[0]][cp[1]] = 'x'

steps = 1
while True:
    steps += 1
    for coord_i, coord in enumerate(nc):
        nc[coord_i] = next_cxns(aoc_data, coord, lc[coord_i])
        lc[coord_i] = coord
    if nc[0] == nc[1]:
        loop_coords[nc[0][0]][nc[0][1]]='x'
        break
    else:
        loop_coords[nc[0][0]][nc[0][1]]='x'
        loop_coords[nc[1][0]][nc[1][1]]='x'

p1_ans = steps
print(p1_ans)

wall_scores = {
    '|': 2,
    '-': 0,
    'F': 1,
    'J': 1,
    'L': -1,
    '7': -1,
    '.': 0
}
wall_scores['S'] = wall_scores[define_s(aoc_data)['shape']]

enclosed_tiles = 0

for r_idx, row in enumerate(loop_coords):
    wall_count = 0
    for t_idx, tile in enumerate(row):
        if tile == 'x':
            wall_count += wall_scores[aoc_data[r_idx][t_idx]]
        elif wall_count % 4 == 2:
            enclosed_tiles += 1

p2_ans = enclosed_tiles
print(p2_ans)