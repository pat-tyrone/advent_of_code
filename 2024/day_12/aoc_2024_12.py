from collections import defaultdict

def fill(grid, region, square, last_step=(0,0), first_square=True):
    region.append(square)
    square_value = grid[square[0]][square[1]]
    h = len(grid)
    w = len(grid[0])
    steps = [(1,0), (-1,0), (0,1), (0,-1)]

    if not first_square:
        steps.remove((last_step[0]*-1, last_step[1]*-1))

    for step in steps:
        new_square = (square[0] + step[0], square[1] + step[1])
        if (not (0 <= new_square[0] < h)) or (not (0 <= new_square[1] < w)):
            continue
        elif new_square in region:
            continue
        elif grid[new_square[0]][new_square[1]] != square_value:
            continue
        else:
            fill(grid, region, new_square, step, False)

def calc_perim(region_dict):
    perim = 0
    for r, col_list in region_dict.items():
        row_total = 0
        for c_idx, c in enumerate(col_list):
            if (c_idx == 0) or (col_list[c_idx - 1] != (c - 1)):
                row_total += 4
            elif col_list[c_idx - 1] == (c - 1):
                row_total += 2
            
            if r != min(region_dict.keys()):
                if c in region_dict[r-1]:
                    row_total += -2
        
        perim += row_total
    
    return perim

def get_switches(region_dict):
    switches = {}
    for r, col_list in region_dict.items():
        switches[r] = {'ons': [col_list[0]], 'offs': [col_list[-1]]}
        for c_idx, c in enumerate(col_list):
            if len(col_list) == 1:
                break

            if (c_idx == 0): # skip the first col in list
                continue
            elif (c == (col_list[c_idx - 1] + 1)): # if its last+1, do nothing
                continue
            else: 
                switches[r]['offs'].append(col_list[c_idx - 1])
                switches[r]['ons'].append(c)
            
        switches[r]['offs'].sort()

    return switches

def calc_sides(region_dict):
    switches = get_switches(region_dict)
    corners = 0
    row_num = min(switches.keys())
    while row_num <= max(switches.keys()):
        for i in range(len(switches[row_num]["ons"])):
            if row_num == min(switches.keys()):
                corners += 4
            else:
                if switches[row_num]["ons"][i] not in switches[row_num - 1]["ons"]:
                    corners += 2
                if switches[row_num]["offs"][i] not in switches[row_num - 1]["offs"]:
                    corners += 2
        # print(f"row_num = {row_num}; corners = {corners}")
        row_num += 1
    return corners

grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.rstrip()))

checked = defaultdict(list)
regions = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if j in checked[i]:
            continue
        else:
            this_region = []
            fill(grid, this_region, (i,j))
            for square in this_region:
                checked[square[0]].append(square[1])
            regions.append(this_region)

p1_ans = 0
p2_ans = 0
for region in regions:
    reg_dict = defaultdict(list)
    for square in region:
        reg_dict[square[0]].append(square[1])
    for col_list in reg_dict.values():
        col_list.sort()
    p1_ans += len(region) * calc_perim(reg_dict)
    p2_ans += len(region) * calc_sides(reg_dict)

print(f"p1_ans: {p1_ans}")
print(f"p2_ans: {p2_ans}")