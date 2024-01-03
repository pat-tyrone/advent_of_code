
directs = []

with open("data.txt") as f:
    for line in f:
        direct = line.rstrip()
        directs.append(direct)

# Part 1
x=0
y=0

# Part 2
aim = 0
y_2 = 0


for direct in directs:
    vec_dir = direct.split(" ")[0]
    vec_mag = int(direct.split(" ")[1])

    if vec_dir == "forward":
        x += vec_mag
        y_2 += vec_mag * aim

    elif vec_dir == "down":
        y += vec_mag
        aim += vec_mag
    else:
        y -= vec_mag
        aim -= vec_mag

print(f"\n\tPart 1 answer: {x*y}")
print(f"\n\tPart 2 answer: {x*y_2}")


