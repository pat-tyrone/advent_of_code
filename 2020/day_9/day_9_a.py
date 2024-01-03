nums = []

with open('input') as input_file:
    for line in input_file:
        nums.append(int(line.rstrip()))

preamble_len = 25
start_pos = 0
next_test = 0

while start_pos < len(nums) - preamble_len: # and do_once <2:

    avail_nums = []
    end_pos = start_pos + preamble_len
    for pos_num in range(start_pos, end_pos):
        avail_nums.append(nums[pos_num])
    
    x=0
    y=1

    # print(avail_nums)
    # print(len(avail_nums))

    keep_going = True

    while keep_going:
        test_sum = avail_nums[x] + avail_nums[y]
        # print(f"\n{avail_nums[x]} + {avail_nums[y]} = {test_sum}?")
        # print(f"{test_sum} = {nums[end_pos]}?")
        # print(test_sum == nums[end_pos])

        if test_sum == nums[end_pos]: #satisfies sum condition; move on to next number
            start_pos += 1
            keep_going = False
            #break
        elif y < len(avail_nums) - 1:
            y += 1
        else:
            x += 1
            y = x + 1
            if x > len(avail_nums) - 2:
                keep_going = False
                print(f"the number that failed the test was {nums[end_pos]}")
                start_pos = len(nums)
                key_num = nums[end_pos]
                break

for value in range(len(nums)):
    contigs = []
    pos = value
    running_sum = 0

    while running_sum < key_num:
        running_sum += nums[pos]
        contigs.append(nums[pos])

        if running_sum != key_num:
            pos += 1
        else:
            print(f"{min(contigs)} + {max(contigs)} = {min(contigs) + max(contigs)}.")

