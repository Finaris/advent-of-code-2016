
file_input = open("input.txt", "r")
directions = [x.strip() for x in file_input.read().split(',')]
blocks = [0, 0, 0, 0]   # North 0, East 1, South 2, West 3
currentDir = 0
Matrix = [[0 for x in range(1000)] for y in range(1000)]
loc = [500, 500]
flag = [False]


def check_dir(dir):
    if dir < 0:
        return dir+4
    elif dir > 3:
        return 0
    else:
        return dir


def check_cell(cell):
    if cell == 1:
        print('HQ at (' + str(loc[0]) + ', ' + str(loc[1]) + ')')
        flag[0] = True
        return True


def fill_cells(steps, face):
    if face == 0:
        for i in range(steps):
            Matrix[loc[0]][loc[1]] = 1
            loc[1] += 1
            blocks[currentDir] += 1
            if check_cell(Matrix[loc[0]][loc[1]]):
                break
    elif face == 1:
        for i in range(steps):
            Matrix[loc[0]][loc[1]] = 1
            loc[0] += 1
            blocks[currentDir] += 1
            if check_cell(Matrix[loc[0]][loc[1]]):
                break
    elif face == 2:
        for i in range(steps):
            Matrix[loc[0]][loc[1]] = 1
            loc[1] -= 1
            blocks[currentDir] += 1
            if check_cell(Matrix[loc[0]][loc[1]]):
                break
    elif face == 3:
        for i in range(steps):
            Matrix[loc[0]][loc[1]] = 1
            loc[0] -= 1
            blocks[currentDir] += 1
            if check_cell(Matrix[loc[0]][loc[1]]):
                break

for move in directions:
    if move[0] == 'R' and not flag[0]:
        currentDir += 1
        currentDir = check_dir(currentDir)
        fill_cells(int(move[1:]), currentDir)
    elif move[0] == 'L' and not flag[0]:
        currentDir -= 1
        currentDir = check_dir(currentDir)
        fill_cells(int(move[1:]), currentDir)
print(blocks)
print(abs(blocks[0]-blocks[2]) + abs(blocks[1]-blocks[3]))

