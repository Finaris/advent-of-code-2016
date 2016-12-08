file_input = open('input.txt', 'r')
puzzle_input = [x.strip() for x in file_input]
count = 0


def is_abba(checker):
    for i in range(len(checker)-3):
        if checker[i] != checker[i+1]:
            if checker[i:i+2] == checker[i+3:i+1:-1]:
                return True
    return False


def support_tls(ip_address):
    list1 = ip_address.split('[')
    list2 = []
    for n in list1:
        if ']' in n:
            temp = n.split(']')
            list2.append(temp[0])
            list2.append(temp[1])
        else:
            list2.append(n)
    for i in range(1, len(list2), 2):
        if is_abba(list2[i]):
            return False
    for i in range(0, len(list2), 2):
        if is_abba(list2[i]):
            return True
    return False

for line in puzzle_input:
    if support_tls(line):
        count += 1
print(count)
