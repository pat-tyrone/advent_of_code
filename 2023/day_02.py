p1_data = []
with open('d2_data.txt') as f:
    for line in f:
        p1_data.append(line.rstrip())


color_max = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

games = []
for game_summary in p1_data:
    game_i = {}
    game_i_number = int(game_summary[:game_summary.index(':')].replace('Game ', ''))
    game_i["game_number"] = game_i_number
    game_i["sets"] = []
    
    game_data = game_summary[game_summary.index(':') + 2:].split('; ')

    for each_set in game_data:
        set_i = each_set.split(', ')
        results_dict = {}
        for each_color in set_i:
            count = int(each_color[:each_color.index(' ')])
            color = each_color[each_color.index(' ') + 1:]
            # print(f"color: {color}; count: {count}")
            results_dict[color] = count
        game_i["sets"].append(results_dict)
    
    games.append(game_i)

p1_answer = 0
p2_answer = 0

# part 1
for g in games:
    # color_mins = {'red': 0, 'green': 0, 'blue': 0}
    is_possible = True
    for set in g["sets"]:
        if not is_possible:
            break
        for color, count in set.items():
            if count > color_max[color]:
                is_possible = False
                break
    if is_possible:
        p1_answer += g["game_number"]

# part 2
for g in games:
    color_mins = {'red': 0, 'green': 0, 'blue': 0}
    for set in g["sets"]:
        for color, count in set.items():
            # print(f"color = {color}; count = {count}")
            color_mins[color] = max(color_mins[color], count)
            # print(color_mins)

    power = 1
    for min in color_mins.values():
        power *= min
    
    p2_answer += power

print(p1_answer)
print(p2_answer)