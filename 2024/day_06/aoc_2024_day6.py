from collections import defaultdict

def record_visits(visit_dict, loc_1, loc_2):
    for r in range(min(loc_1[0], loc_2[0]), max(loc_1[0], loc_2[0])+1):
        for c in range(min(loc_1[1], loc_2[1]), max(loc_1[1], loc_2[1])+1):
            visit_dict[r].add(c)
    
    return visit_dict

def move_guard(guard, grid_dims, row_objects, col_objects):
    loc = guard["loc"]
    gd = guard["dir"]
    oob_row = grid_dims[0]
    oob_col = grid_dims[1]

    dir_steps = {
        '^': (-1,0),
        'v': (1,0),
        '<': (0,-1),
        '>': (0,1)
    }
    turns = {
        '^': '>',
        'v': '<',
        '<': '^',
        '>': 'v'
    }

    if gd in ['^', 'v']: # if guard walking up or down in a column
        objects = [-1] + col_objects[loc[1]] + [oob_row]
        objects.append(loc[0])
        objects.sort()
        row_incr = dir_steps[gd][0] # i.e., (-1,0) for walking up, '^' [-1, 3, 6, 9]
        new_row = objects[objects.index(loc[0]) + row_incr] + (row_incr * -1)
        if new_row in [0, oob_row-1]:
            return {"loc": [new_row, loc[1]], "dir": 'X'}
        else:
            return {"loc": [new_row, loc[1]], "dir": turns[gd]}
    
    elif gd in ['<', '>']: # if guard moving left or right in a row
        objects = [-1] + row_objects[loc[0]] + [oob_col]
        objects.append(loc[1])
        objects.sort()
        col_incr = dir_steps[gd][1] # i.e., (-1,0) for walking up, '^' [-1, 3, 6, 9]
        new_col = objects[objects.index(loc[1]) + col_incr] + (col_incr * -1)
        if new_col in [0,oob_col-1]:
            return {"loc": [loc[0], new_col], "dir": 'X'}
        else:
            return {"loc": [loc[0], new_col], "dir": turns[gd]}
    
    elif gd == 'X':
        return {"loc": loc, "dir": gd}
    else:
        print("something went wrong")
        return None


grid = []
og_guard = {}
row_obs = defaultdict(list)
col_obs = defaultdict(list)
visited = defaultdict(set)

with open('input.txt') as f:
    for row_idx, row in enumerate(f):
        row_list = []
        for col_idx, col in enumerate(row.rstrip()):
            if col in ['^','v','<','>']:
                og_guard["loc"] = [row_idx, col_idx]
                og_guard["dir"] = col
                visited[row_idx].add(col_idx)
            elif col == '#':
                row_obs[row_idx].append(col_idx)
                col_obs[col_idx].append(row_idx)
            row_list.append(col)
        grid.append(row_list)


guard = og_guard.copy()
r = og_guard["loc"][0]
c = og_guard["loc"][1]

while guard["dir"] != 'X':
    old_loc = guard["loc"].copy()
    guard = move_guard(guard, (len(grid), len(grid[0])), row_obs, col_obs)
    new_loc = guard["loc"].copy()
    visited = record_visits(visited, old_loc, new_loc)

p1_ans = 0
for row in list(visited.keys()):
    p1_ans += len(visited[row])

print(f"p1_ans: {p1_ans}")

p2_ans = 0
for r, col_list in visited.items():
    for c in col_list:

        row_obs[r].append(c)
        col_obs[c].append(r)

        guard_turns = defaultdict(list)
        guard = og_guard.copy()
        while guard["dir"] != 'X':
            old_loc = guard["loc"].copy()
            guard = move_guard(guard, (len(grid), len(grid[0])), row_obs, col_obs)
            new_loc = guard["loc"].copy()
            guard_turn = (new_loc[1], guard["dir"])
            if guard_turn in guard_turns[new_loc[0]]:
                p2_ans += 1
                break
            else:
                guard_turns[new_loc[0]].append((new_loc[1], guard["dir"]))
        
        row_obs[r].remove(c)
        col_obs[c].remove(r)

print(f"p2_ans: {p2_ans}")