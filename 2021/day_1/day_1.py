
depths = []

with open("data.txt") as f:
    for line in f:
        depth = int(line.rstrip())
        depths.append(depth)
last = 0
count_incr = -1

for depth in depths:
    if depth > last:
        count_incr += 1
    last = depth

print(f"\n\tPart 1 solution: {count_incr}\n")

count_incr = 0

for i in range(len(depths)):
    try:
        if depths[i] < depths[i+3]:
            count_incr += 1
    except:
        continue

print(f"\n\tPart 2 solution: {count_incr}\n")