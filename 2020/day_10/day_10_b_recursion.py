
jas = []


with open('input') as input_file:
    for line in input_file:
        jas.append(int(line.rstrip()))

# sort the list, so it is in the order that each joltage adapter is connected
jas.sort()
jas.insert(0, 0)
jas.append(max(jas)+3)

# an empty dict to store answers to num_ways to save on calc time
checked = {}

def num_ways(pos):
    """return the number of ways to connect adapter at jas[pos] to device"""

    # print(f"\nchecking pos = {pos}")
    
    # just defining the penultimate adapter so we don't have to type len(jas)-1
    penult = len(jas) - 1

    # define the base case for the recursive function
    if pos == penult:
        return 1
    
    # if we already checked this pos, just retrienve it from the dict
    if pos in checked:
        # print(f"CHECKED[{pos}] = {checked[pos]}")
        return checked[pos]

    total = 0

    # test the next three numbers in jas [pos+1 - pos+3]
    # if we can step from jas[pos] to jas[pos+i], then for that step, add the number of routes
    # from jas[pos+i] to the finish to the running sum variable 'total'
    for i in range(pos+1, min(pos+4, penult+1)):

        # print(f"testing i={i};  pos = {pos}")
        # print(f"jas[i] = {jas[i]}; jas[pos] = {jas[pos]}")

        if jas[i] - jas[pos] <= 3:
            total += num_ways(i)
            # print(f"total is now {total}")
    
    # store the result of the above check in the dict for future reference
    checked[pos] = total

    return total

    

print(num_ways(0))
