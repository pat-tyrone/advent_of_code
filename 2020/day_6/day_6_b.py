
# an empty list to hold the responses to the customs declaration form (cdf)
cdf_responses = []

with open('input') as input_file:
    for line in input_file:
        cdf_responses.append(line.rstrip()) 

# this dummy response is put at the end of cdf_responses so the below while loop knows when to stop
cdf_responses.append("TEMP_LAST_ROW")

# each person's responses are currently one row in the responses.  
# We need to put responses from the same group together. This loop results in one row = one group
# with individuals responses separated by a space
pop_1 = cdf_responses.pop(0)
pop_2 = cdf_responses.pop(0)
while True:
    if pop_2 == "TEMP_LAST_ROW":
        cdf_responses.append(pop_1)
        break

    if pop_2 == "":
        cdf_responses.append(pop_1)
        pop_1 = cdf_responses.pop(0)
        pop_2 = cdf_responses.pop(0)
    else:
        pop_1 = pop_1 + " " + pop_2
        pop_2 = cdf_responses.pop(0)

# empy list to hold responses with all duplicates within a group removed.
cdf_responses_unique = []

#for line in cdf_responses:
#    print(line)

# this loop will remove dupes from each group's responses (i.e. each row in cdf_responses)
for group in cdf_responses:
    unique_responses = []
    for response in group:
        if response not in unique_responses and response != " ":
            unique_responses.append(response)
    cdf_responses_unique.append(unique_responses)

# a list of lists: each sub-list is one individual's 'yes' responses within a group
cdf_responses_ind = []

for group in cdf_responses:
    responses_ind = group.split(" ")
    cdf_responses_ind.append(responses_ind)

new_count = 0

for value in range(465):
    #print(f"group {value} has {len(cdf_responses_ind[value])} people. These were their responses:")
    #print(cdf_responses_ind[value])
    #print("and individually:")
    for response in cdf_responses_unique[value]:
        #print(f"{response} - {cdf_responses[value].count(response)}")
        if cdf_responses[value].count(response) == len(cdf_responses_ind[value]):
            new_count += 1

print(f"the sum of group-question combos for which everyone in that group answered yes \
is {new_count}.")