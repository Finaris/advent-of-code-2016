def is_triangle(sides):
    if int(sides[0]) < int(sides[1]) + int(sides[2]) and int(sides[1]) < int(sides[0]) + int(sides[2])\
            and int(sides[2]) < int(sides[0]) + int(sides[1]):
        return True
    else:
        return False

input_text = open('input.txt', 'r')
triangles = [line.split() for line in input_text]
count = 0
for lists in triangles:
    if is_triangle(lists):
        count += 1
print(count)
