file_input = open("input.txt", "r")
directions = [x.strip() for x in file_input.read().split(',')]
blocks = [0, 0, 0, 0]   # North 0, East 1, South 2, West 3
currentDir = 0


def check_dir(direction):
    if direction < 0:
        return direction + 4
    elif direction > 3:
        return 0
    else:
        return direction

for move in directions:
    if move[0] == 'R':
        currentDir += 1
        currentDir = check_dir(currentDir)
        blocks[currentDir] += int(move[1:])
    elif move[0] == 'L':
        currentDir -= 1
        currentDir = check_dir(currentDir)
        blocks[currentDir] += int(move[1:])
print(abs(blocks[0]-blocks[2]) + abs(blocks[1]-blocks[3]))
