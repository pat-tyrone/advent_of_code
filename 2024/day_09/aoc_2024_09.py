from collections import defaultdict
from copy import deepcopy

blocks = []
with open('input.txt') as f:
    for char in f.read().rstrip():
        blocks.append(int(char))

og_ids = {}
spaces = []
spaces_dict = defaultdict(list)
block_addr = 0
max_id = 0
total_mem_blocks = 0

for i, block_len in enumerate(blocks):
    if i%2 == 0:
        id_num = i // 2
        og_ids[id_num] = [block_addr, block_addr + block_len - 1]
        max_id = id_num
        total_mem_blocks += block_len
    elif block_len==0:
        pass
    else:
        spaces.append([block_addr, block_addr + block_len - 1])
        spaces_dict[block_len].append(block_addr)
    
    block_addr += block_len


# Solves P1
ids = deepcopy(og_ids)
moved_ids = defaultdict(list)
id_to_move = max_id
while True:
    open_spaces = spaces.pop(0)
    mem_blocks = ids[id_to_move]
    size_diff = (open_spaces[1] - open_spaces[0]) - (mem_blocks[1] - mem_blocks[0])

    if size_diff < 0: # if not enough spaces for all id blocks to fit
        moved_ids[id_to_move].append(open_spaces)
        ids[id_to_move][1] = (ids[id_to_move][0] - size_diff - 1)
    elif size_diff == 0: # if perfect fit
        moved_ids[id_to_move].append(open_spaces)
        ids[id_to_move] = []
        id_to_move += -1
    else: # if extra space remains and need to keep filling from next id
        moved_ids[id_to_move].append([open_spaces[0], (open_spaces[0] + mem_blocks[1] - mem_blocks[0])])
        open_spaces = [open_spaces[0] + mem_blocks[1] - mem_blocks[0] + 1, open_spaces[1]]
        spaces.insert(0, open_spaces.copy())
        ids[id_to_move] = []
        id_to_move += -1
    
    if ids[id_to_move][1] == total_mem_blocks - 1:
        break

p1_ans = 0
for id_, block_range in ids.items():
    if block_range == []:
        continue
    for i in range(block_range[0], block_range[1]+1):
        p1_ans += (id_ * i)

for id_, block_range_lol in moved_ids.items():
    for block_range in block_range_lol:
        for i in range(block_range[0], block_range[1]+1):
            p1_ans += (id_ * i)

print(f"p1_ans = {p1_ans}")


# solves p2
ids = deepcopy(og_ids)
id_to_move = max_id

while True:
    mem_blocks = ids[id_to_move]
    new_addr = mem_blocks[0]
    dest_size = 0
    block_len = mem_blocks[1] - mem_blocks[0] + 1
    move_block = False
    to_delete = []
    for space_len, addresses in spaces_dict.items():
        if not addresses:
            to_delete.append(space_len)
        elif addresses[0] > mem_blocks[0]:
            # if this space_len only exists to the right of the mem_block i'm looking at, it won't be eligible for later mem-blocks, so delete:
            to_delete.append(space_len)
        elif (space_len >= block_len) and addresses[0] < new_addr:
            # if above is true, then block gets moved, but only after exiting this for loop
            new_addr = addresses[0]
            dest_size = space_len
            move_block = True
        else:
            pass

    if move_block and dest_size == block_len:
        ids[id_to_move] = [new_addr, (new_addr + block_len - 1)]
        del spaces_dict[dest_size][0]
        if not spaces_dict[dest_size]:
            to_delete.append(dest_size)
    elif move_block:
        ids[id_to_move] = [new_addr, (new_addr + block_len - 1)]
        spaces_dict[dest_size - block_len].append((new_addr + block_len))
        spaces_dict[dest_size - block_len].sort()
        del spaces_dict[dest_size][0]
        if not spaces_dict[dest_size]:
            to_delete.append(dest_size)
    else:
        pass

    for space_len_to_delete in to_delete:
        del spaces_dict[space_len_to_delete]

    move_block = False
    id_to_move += -1
    if id_to_move == 0:
        break

p2_ans = 0
for id_, block_range in ids.items():
    if block_range == []:
        continue
    for i in range(block_range[0], block_range[1]+1):
        p2_ans += (id_ * i)

print(f"p2_ans = {p2_ans}")