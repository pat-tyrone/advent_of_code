from collections import defaultdict

def count_stones(stone, blink_count, results_dict):
    """takes a stone (int) as input and returns the new count of stones after some given blink_count (int)"""
    try:
        result = results_dict[stone][blink_count]
        return result
    except:
        if (blink_count == 1) and (len(str(stone)) % 2 == 0):
            results_dict[stone][blink_count] = 2
            return 2
        elif blink_count == 1:
            results_dict[stone][blink_count] = 1
            return 1
        else:
            new_stones = []
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stone_len = len(str(stone)) // 2
                new_stones.append(int(str(stone)[:(new_stone_len)]))
                new_stones.append(int(str(stone)[new_stone_len:]))
            else:
                new_stones.append(stone * 2024)
            
            result = 0
            for new_stone in new_stones:
                result += count_stones(new_stone, blink_count-1, results_dict)

            results_dict[stone][blink_count] = result
            return result

with open('input.txt') as f:
    stones = [int(x) for x in f.read().split()]

p1_ans = 0
p2_ans = 0
stone_results = defaultdict(dict)
for stone in stones:
    p1_ans += count_stones(stone, 25, stone_results)
    p2_ans += count_stones(stone, 75, stone_results)

print(f"p1_ans: {p1_ans}")
print(f"p2_ans: {p2_ans}")