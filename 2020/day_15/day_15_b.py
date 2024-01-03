
input_ = [6,13,1,15,2,0]

def solve_p2(starting_nums, num_turns):

    pos_dict = {}
    for value in range(len(starting_nums)):
        pos_dict[starting_nums[value]] = value + 1

    counter = len(starting_nums)

    ns_post = None
    last = starting_nums[-1]

    for value in range(num_turns-counter):

        counter += 1

        if last in pos_dict.keys():
            ns_post = counter - pos_dict[last] - 1
        
        else:
            ns_post = 0
           
        pos_dict[last] = counter - 1
        last = ns_post

    return (ns_post)

print(solve_p2(input_, 30000000))