with open ('input.txt') as f:
    data = [line.rstrip() for line in f.readlines()]

L = []
R = []
for row in data:
    row_split = row.split()
    L.append(int(row_split[0]))
    R.append(int(row_split[1]))
L.sort()
R.sort()

total_dist = 0
for i in range(len(L)):
    total_dist += abs(L[i] - R[i])

sim_dict = {}

for num in L:
    if num not in sim_dict.keys():
        sim_dict[num] = [1, 0]
    else:
        sim_dict[num][0] += 1

for num in R:
    if num not in sim_dict.keys():
        sim_dict[num] = [0, 1]
    else:
        sim_dict[num][1] += 1

sim_score = 0
for num in sim_dict.keys():
    sim_score += (num * sim_dict[num][0] * sim_dict[num][1])


print(f"Part 1 answer: {total_dist}")
print(f"Part 2 answer: {sim_score}")
