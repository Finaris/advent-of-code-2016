import itertools
import collections


def is_triangle(sides):
    if int(sides[0]) < int(sides[1]) + int(sides[2]) and int(sides[1]) < int(sides[0]) + int(sides[2])\
            and int(sides[2]) < int(sides[0]) + int(sides[1]):
        return True
    else:
        return False

input_text = open('input.txt', 'r')
triangles = [line.split() for line in input_text]
triangles = list(itertools.chain.from_iterable(triangles))
column1 = collections.deque()
column2 = collections.deque()
column3 = collections.deque()
for i in range(len(triangles)):
    if i % 3 == 0:
        column1.append(triangles[i])
    elif i % 3 == 1:
        column3.append(triangles[i])
    elif i % 3 == 2:
        column2.append(triangles[i])
count = 0
for i in range(0, len(triangles)//3, 3):
    if is_triangle([column1.pop(), column1.pop(), column1.pop()]):
        count += 1
    if is_triangle([column2.pop(), column2.pop(), column2.pop()]):
        count += 1
    if is_triangle([column3.pop(), column3.pop(), column3.pop()]):
        count += 1
print(count)
