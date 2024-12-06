def check_let_p1(grid, coord, direction=(0,1), word_part=''):
    word = word_part
    row = coord[0]
    col = coord[1]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    if (row<0) or (col<0) or (row>=len(grid)) or (col>=len(grid[0])):
        return 0
    
    if (word == 'XMA') and (grid[row][col] == 'S'):
        return 1
    elif (word == 'XMA'):
        return 0
    elif word == 'XM'and (grid[row][col] == 'A'):
        return check_let_p1(grid, (row+direction[0], col+direction[1]), direction, 'XMA')
    elif word == 'XM':
        return 0
    elif word == 'X'and (grid[row][col] == 'M'):
        return check_let_p1(grid, (row+direction[0], col+direction[1]), direction, 'XM')
    elif word == 'X':
        return 0
    elif word == ''and (grid[row][col] == 'X'):
        cnt = 0
        for step_dir in directions:
            cnt += check_let_p1(grid, (row+step_dir[0], col+step_dir[1]), step_dir, 'X')
        return cnt
    elif word == '':
        return 0

def check_let_p2(grid, coord):
    row = coord[0]
    col = coord[1]
    ltr = grid[row][col]

    if (not 0 < row < len(grid)-1) or (not 0 < col < len(grid[0])-1):
        return 0
    elif ltr != 'A':
        return 0
    else:
        diag_1 = [grid[row+1][col+1], grid[row-1][col-1]]
        diag_2 = [grid[row+1][col-1], grid[row-1][col+1]]
        if (set(diag_1) == {'M', 'S'}) and (set(diag_2) == {'M', 'S'}):
            return 1
        else:
            return 0


xmas_grid = []
with open('input.txt') as f:
    for line in f:
        lol = []
        for letter in line.rstrip():
            lol.append(letter)
        xmas_grid.append(lol)

word_cnt = 0
x_cnt = 0
for i in range(len(xmas_grid)):
    for j in range(len(xmas_grid[0])):
        word_cnt += check_let_p1(xmas_grid, (i,j))
        x_cnt += check_let_p2(xmas_grid, (i,j))

print(f"p1 ans: {word_cnt}")
print(f"p2 ans: {x_cnt}")