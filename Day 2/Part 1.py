Matrix = [[0 for x in range(3)] for y in range(3)]
input_text = open('input.txt', 'r')
movements = [x.strip() for x in input_text]
location = [1, 1]
up_constraints = [1, 2, 3]
down_constraints = [7, 8, 9]
left_constraints = [1, 4, 7]
right_constraints = [3, 6, 9]


def fill_keypad():
    Matrix[0][0] = 7
    Matrix[1][0] = 8
    Matrix[2][0] = 9
    Matrix[0][1] = 4
    Matrix[1][1] = 5
    Matrix[2][1] = 6
    Matrix[0][2] = 1
    Matrix[1][2] = 2
    Matrix[2][2] = 3

fill_keypad()
for steps in movements:
    for char in steps:
        if char == 'U':
            if not Matrix[location[0]][location[1]] in up_constraints:
                location[1] += 1
        elif char == 'L':
            if not Matrix[location[0]][location[1]] in left_constraints:
                location[0] -= 1
        elif char == 'R':
            if not Matrix[location[0]][location[1]] in right_constraints:
                location[0] += 1
        elif char == 'D':
            if not Matrix[location[0]][location[1]] in down_constraints:
                location[1] -= 1
        else:
            print('Error!')
    print(Matrix[location[0]][location[1]], end='')

