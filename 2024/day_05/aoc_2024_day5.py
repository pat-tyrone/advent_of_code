def is_even(n):
    return n%2==0

def list_pos_swap(before_list, old_idx, new_idx):
    after_list = before_list
    item_to_move = after_list.pop(old_idx)
    after_list.insert(new_idx, item_to_move)
    return after_list

def middle_index(list):
    return int((len(list) + len(list)%2) / 2) - 1

ord_dict = {}
updates = []
with open('input.txt') as f:
    order_line = True
    for line in f:
        if len(line.rstrip()) == 0:
            order_line = False
            continue
        if order_line:
            ord_constraint = [int(x) for x in line.rstrip().split('|')]
            if ord_constraint[0] in ord_dict.keys():
                ord_dict[ord_constraint[0]].append(ord_constraint[1])
            else:
                ord_dict[ord_constraint[0]] = [ord_constraint[1]]
        else:
            updates.append([int(page) for page in line.rstrip().split(',')])

p1_ans = 0
p2_ans = 0
for update in updates:
    fixed_update = update.copy()
    passed = []
    for i, x in enumerate(update):
        if i==0:
            pass
        else:
            new_idx = i
            try:
                cannot_pass = set(ord_dict[x])
                for viol in cannot_pass.intersection(set(passed)):
                    new_idx = min(new_idx, fixed_update.index(viol))
                fixed_update = list_pos_swap(fixed_update, i, new_idx)
            except:
                pass
        
        passed.append(x)
    
    if fixed_update == update:
        p1_ans += update[middle_index(update)]
    else:
        p2_ans += fixed_update[middle_index(fixed_update)]

print(f"p1 ans: {p1_ans}")
print(f"p2 ans: {p2_ans}")