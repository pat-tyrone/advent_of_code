topo_map = []
with open('input.txt') as f:
    for line in f:
        topo_map.append([int(x) for x in list(line.rstrip())])

def get_score(grid, addr, nines):
    # print(f"\naddr = {addr}; y = {grid[addr[0]][addr[1]]}")
    if (grid[addr[0]][addr[1]] == 9) and (addr not in nines):
        nines.append(addr)
        return 1
    elif grid[addr[0]][addr[1]] == 9:
        return 0

    return_score = 0

    next_steps = [(addr[0], addr[1]+1), (addr[0], addr[1]-1), (addr[0]+1, addr[1]), (addr[0]-1, addr[1])]
    for ns in next_steps:
        if not 0 <= ns[0] < len(grid):
            continue
        elif not 0 <= ns[1] < len(grid[0]):
            continue
        elif grid[ns[0]][ns[1]] == grid[addr[0]][addr[1]] + 1:
            # print(f"ELIF ns = {ns}")
            return_score += get_score(grid, ns, nines)
        else:
            # print(f"ELSE ns: {ns}")
            continue
    
    return return_score

def get_score_p2(grid, addr, nines):
    # print(f"\naddr = {addr}; y = {grid[addr[0]][addr[1]]}")
    if (grid[addr[0]][addr[1]] == 9):
        return 1

    return_score = 0

    next_steps = [(addr[0], addr[1]+1), (addr[0], addr[1]-1), (addr[0]+1, addr[1]), (addr[0]-1, addr[1])]
    for ns in next_steps:
        if not 0 <= ns[0] < len(grid):
            continue
        elif not 0 <= ns[1] < len(grid[0]):
            continue
        elif grid[ns[0]][ns[1]] == grid[addr[0]][addr[1]] + 1:
            # print(f"ELIF ns = {ns}")
            return_score += get_score_p2(grid, ns, nines)
        else:
            # print(f"ELSE ns: {ns}")
            continue
    
    return return_score

p1_ans = 0
p2_ans = 0
for i in range(len(topo_map)):
    for j in range(len(topo_map[i])):
        if topo_map[i][j] == 0:
            niners = []
            p1_ans += get_score(topo_map, (i,j), niners)
            p2_ans += get_score_p2(topo_map, (i,j), niners)

print(f"p1_ans: {p1_ans}")
print(f"p2_ans: {p2_ans}")