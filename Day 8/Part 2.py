file_input = open('input.txt', 'r')
puzzle_input = [x.strip() for x in file_input]
display = [[0 for _ in range(50)] for __ in range(6)]


# Created for testing purposes
def print_display():
    [print(line) for line in display]
    print()


def parse_command(command):
    global display
    instructions = command.split(' ')
    if command[0:4] == 'rect':
        dimensions = instructions[1].split('x')
        for i in range(int(dimensions[0])):
            for j in range(int(dimensions[1])):
                display[j][i] = 1
    elif command[0:10] == 'rotate row':
        row = int((instructions[2])[2:len(instructions[2])])
        shift_num = int(instructions[4])
        temp_display = [[x for x in display[y]] for y in range(len(display))]
        for i in range(len(temp_display[0])):
            temp_display[row][i] = 0
        for i in range(len(display[0])):
            if display[row][i] == 1:
                temp_display[row][(i + shift_num) % len(display[0])] = 1
        display = temp_display

    elif command[0:13] == 'rotate column':
        column = int((instructions[2])[2:len(instructions[2])])
        shift_num = int(instructions[4])
        temp_display = [[x for x in display[y]] for y in range(len(display))]
        for i in range(len(temp_display)):
            temp_display[i][column] = 0
        for i in range(len(display)):
            if display[i][column] == 1:
                temp_display[(i+shift_num) % len(display)][column] = 1
        display = temp_display

    else:
        print('Could not parse command.')

[parse_command(line) for line in puzzle_input]
count = 0
for i in display:
    for n in i:
        if n == 1:
            count += 1
print(count)
print_display()     # Just run this command and read off --> ZJHRKCPLYJ
