
from dataclasses import replace


puzz_input = []

with open("data.txt") as f:
    for line in f:
        puzz_input.append(line.rstrip())

# create the nums_called list as a list of integers
nums_called = puzz_input[0].split(",")
for i in range(len(nums_called)):
    nums_called[i] = int(nums_called[i])

boards = [[]]

for row in puzz_input[2:]:
    if len(row) == 0:
        boards.append([])
    else:
        last_board = (len(boards) - 1)
        split_str = row.split(" ")
        split_str[:] = [x for x in split_str if x != '']
        for x in split_str:
            boards[last_board].append(int(x))


def check_board(board, nums):
    """checks if a board has BINGO based on the nums called
    returns the turn on which BINGO was made, or returns 0 if no BINGO"""
    rows_hit = []
    cols_hit = []

    for num in nums:
        try:
            print(f"{num} is at index {board.index(num)}")
        except:
            print(f"{num} is not on the board")

print(nums_called)
print(boards[0])
check_board(boards[0], nums_called)



