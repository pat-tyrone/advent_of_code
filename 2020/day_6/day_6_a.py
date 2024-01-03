
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


# soy = "sum of yes" responses.  soy_group will be used to sum the total questions that 
# someone answered 'yes' for--max 1 yes per group
soy_group = 0

for group in cdf_responses_unique:
    soy_group += len(group)

print(f"Counting affirmative responses to each question only once per group, the total number \
of affirmative responses was {soy_group}.")