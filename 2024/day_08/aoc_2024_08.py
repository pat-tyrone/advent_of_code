from collections import defaultdict

def get_antinodes(a1, a2, oob_row, oob_col):
    distance = ((a1[0]-a2[0]), (a1[1]-a2[1]))
    antinodes = []
    
    anti_1 = ((a1[0]+distance[0]), (a1[1]+distance[1]))
    if (0 <= anti_1[0] < oob_row) and (0 <= anti_1[1] < oob_col):
        antinodes.append(anti_1)
    
    anti_2 = ((a2[0]-distance[0]), (a2[1]-distance[1]))
    if (0 <= anti_2[0] < oob_row) and (0 <= anti_2[1] < oob_col):
        antinodes.append(anti_2)
    
    return antinodes

def get_antinodes_p2(a1, a2, oob_row, oob_col):
    distance = ((a1[0]-a2[0]), (a1[1]-a2[1]))
    antinodes = [a1, a2]
    
    anti_1 = a1
    while True:
        anti_1 = ((anti_1[0]+distance[0]), (anti_1[1]+distance[1]))
        if (0 <= anti_1[0] < oob_row) and (0 <= anti_1[1] < oob_col):
            antinodes.append(anti_1)
        else:
            break
    
    anti_2 = a2
    while True:
        anti_2 = ((anti_2[0]-distance[0]), (anti_2[1]-distance[1]))
        if (0 <= anti_2[0] < oob_row) and (0 <= anti_2[1] < oob_col):
            antinodes.append(anti_2)
        else:
            break
    return antinodes

grid = []
freqs = defaultdict(list)
with open('input.txt') as f:
    for r, line in enumerate(f):
        row = list(line.rstrip())
        grid.append(row)
        for c, char in enumerate(row):
            if char != '.':
                freqs[char].append((r,c))

h = len(grid)
w = len(grid[0])

antis_1 = set()
antis_2 = set()
for freq, ant_list in freqs.items():
    for i, ant_i in enumerate(ant_list):
        for j, ant_j in enumerate(ant_list):
            if i == j:
                continue
            antis_1 = antis_1.union(set(get_antinodes(ant_i, ant_j, h, w)))
            antis_2 = antis_2.union(set(get_antinodes_p2(ant_i, ant_j, h, w)))
   
print(f"p1_ans = {len(antis_1)}")
print(f"p2_ans = {len(antis_2)}")