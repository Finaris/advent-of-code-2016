file_input = open('input.txt', 'r')   # There are 624 rows and 8 columns
puzzle_input = [x.strip() for x in file_input]
most_common = [[0 for a in range(26)] for b in range(8)]
for line in puzzle_input:
    for i in range(len(line)):
        most_common[i][ord(line[i:i + 1]) - 97] += 1
answer = ''
for sub in most_common:
    min_index = 0
    min_val = 100
    count = 0
    for e in sub:
        if e < min_val:
            min_index = count
            min_val = e
        count += 1
    answer += chr(min_index+97)
print(answer)
