
# class AdArr:
#     """a class to model possible adapter arrangements"""
#     def __init__(self, wall_joltage, device_joltage, adapters=[]):
#         """initialize the arrangement"""
#         self.adapters = adapters[:]
#         self.wall_joltage = wall_joltage
#         self.device_joltage = device_joltage
    
#     def test_arr(self):
#         """returns true if adapter arrangement will work"""
        
#         arr = self.adapters
#         arr.sort()
#         arr.insert(0, self.wall_joltage)
#         arr.append(self.device_joltage)

#         diffs = []

#         for value in range(1, len(arr)):
#             diff = arr[value] - arr[value -1]
#             diffs.append(diff)
        
#         if min(diffs) >= 1 and max(diffs) <= 3:
#             return True
#         else:
#             return False


jas = []


with open('input') as input_file:
    for line in input_file:
        jas.append(int(line.rstrip()))

# sort the list, so it is in the order that each joltage adapter is connected
jas.sort()

device_joltage = jas[-1] + 3
print(f"device_joltage = {device_joltage}\n")

#empty list of lists.  each sub list will be a list of adapters to form a class instance of AdArr
ad_arrs = []

#populates ad_arrs with one sub_list so the next while loop can start
for ad in jas:
    # print(ad)
    if ad <= 3:
        new_ad_arr = []
        new_ad_arr.append(ad)
        ad_arrs.append(new_ad_arr)
    else:
        break

# print(f"ad_arrs AT START: {ad_arrs}")

no_appends = 0

while True:

    new_arr_count = 0
    
    curr_arr = ad_arrs.pop(0)
    # print(f"\n***MAIN WHILE BLOCK***\ncurr_arr: {curr_arr}")
    
    if jas.index(curr_arr[-1])+1 != len(jas):

        ad_rem = jas[jas.index(curr_arr[-1])+1:len(jas)]
        # print(f"\tad_rem: {ad_rem}")

        xyz = curr_arr[:]
        xyz.append(ad_rem[0])
        # print(f"xyz: {xyz}")
        if xyz in ad_arrs:
            ad_arrs.append(curr_arr)
            # print(f"\n\t\t\tad_arrs RESTORED: {ad_arrs}")
            continue

        for ad in ad_rem:
            diff = ad - max(curr_arr)
            # print("\n***FOR BLOCK***")
            

            if diff >= 1 and diff <= 3:
                # print("***FOR IF***")
                new_arr = curr_arr[:]
                new_arr.append(ad)
                # print(f"\t\tnew_arr APPENDED: {new_arr})")
                ad_arrs.append(new_arr)
                new_arr_count += 1
                # print(f"\t\t\tad_arrs: {ad_arrs}")

                if ad == ad_rem[-1]:
                    ad_arrs.append(curr_arr)
                    # print(f"\t\t\tad_arrs RESTORED: {ad_arrs}")

            else:
                # print("***FOR ELSE***")
                ad_arrs.append(curr_arr)
                # print(f"\t\t\tad_arrs RESTORED: {ad_arrs}")
                break
        
    else:
        ad_arrs.append(curr_arr)
        # print("\n***WHILE ELSE***")
        # print(f"ad_arrs RESTORED: {ad_arrs} \n\tLENGTH = {len(ad_arrs)}")

    if new_arr_count == 0:
        no_appends += 1

        if no_appends == len(ad_arrs):
            # print(ad_arrs)
            # print(len(ad_arrs))
            break

# print(f"\nad_arrs START: {ad_arrs}\n")

for value in range(len(ad_arrs)):
    test_arr = ad_arrs.pop(0)
    if test_arr[0] > 3 or test_arr[-1] < device_joltage - 3:
        continue
    else:
        ad_arrs.append(test_arr)

# print(ad_arrs)

# for arr in ad_arrs:
#     print(arr)
print(len(ad_arrs))

