aoc_data = []
with open('data_09.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())


def row_as_lol(space_delim_str):
    return [[int(i) for i in space_delim_str.split()]]

def next_hist(hist_list):
    nh = []
    for i in range(len(hist_list)):
        if i == 0:
            continue
        else:
            nh.append(hist_list[i] - hist_list[i-1])
    return nh

def full_hist(hist_lol):
    this_row = hist_lol[-1]
    if all(num == 0 for num in this_row):
        return hist_lol
    else:
        hist_lol.append(next_hist(this_row))
        return full_hist(hist_lol)

def extrap(full_hist):
    x = 0
    for row in reversed(full_hist[:-1]):
        y = row[-1]
        x += y
    return x

def extrap_p2(full_hist):
    x = 0
    for row in reversed(full_hist[:-1]):
        y = row[0]
        x = y - x
    return x

p1_ans = 0
p2_ans = 0
for row in aoc_data:
    int_lol = row_as_lol(row)
    fh = full_hist(int_lol)
    p1_ans += extrap(fh)
    p2_ans += extrap_p2(fh)

print(p1_ans)
print(p2_ans)