
input_ = [6,13,1,15,2,0]

def solve_p1(starting_nums, num_turns):

    mem = []
    counter = 0

    ns_pre = None
    ns_post = None

    for value in range(num_turns):

        counter += 1
        #print(f"counter = {counter}")
            
        if value < len(starting_nums):
            ns_pre = starting_nums[value]
            ns_post = ns_pre
            mem.append(ns_post)
                    
        else:
            ns_pre = mem.pop(-1)

            if ns_pre in mem:
                ns_post = mem[::-1].index(ns_pre) + 1
            else:
                ns_post = 0
            
            mem.append(ns_pre)
            mem.append(ns_post)


        #print(f"\tns_pre = {ns_pre}")
        #print(f"\tns_post = {ns_post}")

    return (ns_post)

print(solve_p1(input_, 2020))