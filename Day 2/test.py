Matrix = [[0 for x in range(5)] for y in range(5)]
input_text = open('input.txt', 'r')
movements = [x.strip() for x in input_text]
location = [0, 2]
up_constraints = [5, 2, 1, 4, 9]
down_constraints = [5, 9, 'A', 'C', 'D']
left_constraints = [1, 2, 5, 'A', 'D']
right_constraints = [1, 4, 9, 'C', 'D']


def fill_keypad():
    Matrix[0][2] = 5
    Matrix[1][2] = 6
    Matrix[2][2] = 7
    Matrix[3][2] = 8
    Matrix[4][2] = 9
    Matrix[1][3] = 2
    Matrix[2][3] = 3
    Matrix[3][3] = 4
    Matrix[2][4] = 1
    Matrix[1][1] = 'A'
    Matrix[2][1] = 'B'
    Matrix[3][1] = 'C'
    Matrix[2][0] = 'D'

fill_keypad()
# test_case = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
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
