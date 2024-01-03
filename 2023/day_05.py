aoc_data = []
with open('d05_data.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())

def get_next_num(num, mp_lol, walk_forward=True, skip_range=0):
    if walk_forward:
        from_idx = 1
        to_idx = 0
    else:
        from_idx = 0
        to_idx = 1

    new_num = num

    for mp_list in mp_lol:
        if num >= mp_list[from_idx] + mp_list[2]:
            continue
        elif num >= mp_list[from_idx]:
            new_num = mp_list[to_idx] + (num - mp_list[from_idx])
            skip_range = mp_list[2] - (num - mp_list[from_idx]) - 1
            break
        else:
            break
    
    return (new_num, skip_range)

def walk_map(dict, num, walk_forward=True, ck_idx=0, skip_range=99999999999999999999999999):
    ck = list(dict.keys())[ck_idx]
    if walk_forward:
        key_incr = 1
        last_key_idx = len(list(dict.keys())) - 1
    else:
        key_incr = -1
        last_key_idx = 0
    
    next_num_tuple = get_next_num(num, dict[ck], walk_forward)
    new_num = next_num_tuple[0]
    skip_range = min(skip_range, next_num_tuple[1])

    if ck_idx == last_key_idx:
        # print(f"num={num}; new_num={new_num}")
        return (new_num, skip_range)
    else:
        return walk_map(dict, new_num, walk_forward, ck_idx+key_incr, skip_range)


list_dict = {}
for line in aoc_data[2:]:
    if len(line) == 0:
        pass
    elif not line[0].isdigit():
        current_key = line.replace(' map:', '')
        if current_key not in list_dict.keys():
            list_dict[current_key] = []
    else:
        list_dict[current_key].append([int(mp) for mp in line.split()])

# sort list_dict on "from" column, since walk_fwd=True
for k, v in list_dict.items():
    list_dict[k] = sorted(v, key=lambda x: x[1])

seeds_p1 = [int(seed) for seed in aoc_data[0].split(': ')[1].split()]

p1_ans = 999999999999
for seed in seeds_p1:
    p1_ans = min(p1_ans, walk_map(list_dict, seed)[0])
print(p1_ans)

# sort list_dict on "to" column, since walk_fwd=False
for k, v in list_dict.items():
    list_dict[k] = sorted(v, key=lambda x: x[0])

# create and sort seed numbers for p2
seeds_p2 = []
seed_i = 0
for range_bound in aoc_data[0].split(': ')[1].split():
    if seed_i % 2 == 0:
        seed_range = [int(range_bound), 0]
    else:
        seed_range[1] = int(range_bound)
        seeds_p2.append(seed_range)
    seed_i += 1
seeds_p2 = sorted(seeds_p2, key=lambda x: x[0])


seed_found = False
loc_i = 0
while not seed_found:
    seed_num_tup = walk_map(list_dict, loc_i, False, 6)
    seed_num = seed_num_tup[0]

    for seed_bounds in seeds_p2:
        if seed_num >= seed_bounds[0] + seed_bounds[1]:
            continue
        elif seed_num >= seed_bounds[0]:
            seed_found = True
            p2_answer = loc_i
            print(p2_answer)
            break
        else:
            break
    
    loc_i += 1 + seed_num_tup[1]