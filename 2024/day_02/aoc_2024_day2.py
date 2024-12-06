import numpy as np

def check_safety(levs, rerun=False):
    """
    levs: list of integers
    rerun: boolean
    """
    safe = True
    step_vals = []
    for i in range(1, len(levs)):
        step_vals.append(levs[i] - levs[i-1])
    
    prob_step_indices = []
    for i, step_val in enumerate(step_vals):
        if (np.sign(step_val) != np.sign(step_vals[i-1])) or (abs(step_val) not in [1,2,3]):
            prob_step_indices.extend([i, i+1])

    if bool(prob_step_indices) and rerun:
        return (False, False)
    elif bool(prob_step_indices):
        lev_rem_indices = set(prob_step_indices) # indices of levels to remove and call recursively
        for rem_idx in lev_rem_indices:
            levs_copy = levs.copy()
            del levs_copy[rem_idx]
            safe = check_safety(levs_copy, True)[1]
            if safe:
                break
        return (False, safe)
    else:
        return (not rerun, True)

reps = []
with open('input.txt') as f:
    for line in f:
        reps.append(line.strip())

safe_cnt_1 = 0
safe_cnt_2 = 0
for report in reps:
    levels = [int(lev) for lev in report.split()]
    safety_tuple = check_safety(levels)
    if safety_tuple[0]:
        safe_cnt_1 += 1
    if safety_tuple[1]:
        safe_cnt_2 += 1

print(f"p1 ans = {safe_cnt_1}")
print(f"p2 ans = {safe_cnt_2}")