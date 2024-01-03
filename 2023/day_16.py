import sys
sys.setrecursionlimit(100000) 

def illum_grid(grid_lol, rc, dir, dir_dict, lit_set=set()):
    """sends light through grid; returns list of illuminated (r,c) tuples"""
    if rc[0] <0 or rc[1] < 0:
        return []
    else:
        try:
            rc_val = grid_lol[rc[0]][rc[1]]
        except:
            # if we pass a rc value outside bounds of grid, then no further recursive calls
            return []
        
    

    illuminated = [(rc[0], rc[1])]
    lit_set.add(((rc[0], rc[1]), (dir[0], dir[1])))
    
    next_rc_list = []
    for i, next_dir in enumerate(dir_dict[dir][rc_val]):
        # list of tuples is next_rc coordinates and direction
        next_rc_list.append([(rc[0]+next_dir[0], rc[1]+next_dir[1]), (next_dir[0], next_dir[1])])
    
    for next_rc in next_rc_list:
        if ((next_rc[0][0], next_rc[0][1]), (next_rc[1][0], next_rc[1][1])) in lit_set:
            continue
        illuminated.extend(illum_grid(grid_lol, (next_rc[0][0], next_rc[0][1]), (next_rc[1][0], next_rc[1][1]), dir_dict, lit_set))

    return set(illuminated)

aoc_data = []
with open('example_16.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())

dir_dict = {
    (1, 0): { # moving down
        '.': [(1, 0)],
        '/': [(0, -1)],
        '\\': [(0, 1)],
        '-': [(0, 1), (0, -1)],
        '|': [(1, 0)]
    },
    (-1, 0): { # moving up
        '.': [(-1, 0)],
        '/': [(0, 1)],
        '\\': [(0, -1)],
        '-': [(0, 1), (0, -1)],
        '|': [(-1, 0)]
    },
    (0, 1): { # moving right
        '.': [(0, 1)],
        '/': [(-1, 0)],
        '\\': [(1, 0)],
        '-': [(0, 1)],
        '|': [(1, 0), (-1, 0)]
    },
    (0, -1): { # moving left
        '.': [(0, -1)],
        '/': [(1, 0)],
        '\\': [(-1, 0)],
        '-': [(0, -1)],
        '|': [(1, 0), (-1, 0)]
    }
}


p1_ans = len(illum_grid(aoc_data, (0,0), (0,1), dir_dict))
print(p1_ans)

# TOP
p2_ans = 0
for j in range(len(aoc_data[0])):
    lit_list = set()
    lit_list = illum_grid(aoc_data, (0,j), (1,0), dir_dict, set())
    p2_ans = max(p2_ans, len(lit_list))

# BOTTOM
for i in range(len(aoc_data[0])):
    lit_list = illum_grid(aoc_data, (len(aoc_data[0])-1,i), (-1,0), dir_dict, set())
    p2_ans = max(p2_ans, len(lit_list))

# LEFT
for i in range(len(aoc_data)):
    lit_list = illum_grid(aoc_data, (i,0), (0,1), dir_dict, set())
    p2_ans = max(p2_ans, len(lit_list))

# RIGHT
for i in range(len(aoc_data)):
    lit_list = illum_grid(aoc_data, (i,len(aoc_data)-1), (0,-1), dir_dict, set())
    p2_ans = max(p2_ans, len(lit_list))

print(p2_ans)