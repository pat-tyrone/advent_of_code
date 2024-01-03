aoc_data = []
with open('d06_data.txt') as f:
    for line in f:
        aoc_data.append(line.rstrip())


times = [int(time) for time in aoc_data[0].split(":")[1].strip().split()]
distances = [int(x) for x in aoc_data[1].split(":")[1].strip().split()]

def beat_record(t, d):

    winning_nums = []
    for i in range(1, t+1):
        boat_distance = i * (t - i)
        if boat_distance > d:
            winning_nums.append(i)
    return winning_nums

p1_ans = 1
for i in range(len(times)):
    num_ways = len(beat_record(times[i], distances[i]))
    p1_ans *= num_ways
print(p1_ans)

time_p2 = 44826981
distance_p2 = 202107611381458

# time_p2 = 71530
# distance_p2 = 940200

def min_max_win(t, d):
    min_max = []
    for i in range(1, t+1):
        boat_distance = i * (t - i)
        if boat_distance > d:
            min_max.append(i)
            break
    
    for i in range(t):
        boat_distance = (t - i) * (t - (t - i))
        if boat_distance > d:
            min_max.append((t - i))
            break    
    
    return min_max

p2_ans = min_max_win(time_p2, distance_p2)
print(p2_ans[1] - p2_ans[0] + 1)
