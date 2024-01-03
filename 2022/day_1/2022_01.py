with open('input.txt') as f:
    elves = f.read().split('\n\n')
    f.close()

def count_cals(elf):
    food_list = elf.split('\n')
    cals = 0
    for food in food_list:
        food_int = int(food)
        cals += food_int
    return cals

max_cals = 0
top_3 = [0,0,0]

for elf in elves:
    elf_cals = count_cals(elf)
    if elf_cals > max_cals:
        max_cals = elf_cals
    
    rank_3 = min(top_3)
    if elf_cals > rank_3:
        top_3.remove(rank_3)
        top_3.append(elf_cals)

print(f"part 1: {max_cals}")

top_3_sum = 0
for i in top_3:
    top_3_sum += i

print(f"part 2: {top_3_sum}")