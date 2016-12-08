file_input = open('input.txt', 'r')
puzzle_input = [x.strip() for x in file_input]
count = 0


def get_aba(checker):
    temp_list = []
    for i in range(len(checker)-2):
        if checker[i] == checker[i+2]:
            temp_list.append(checker[i:i+3])
    return temp_list


def is_bab(to_check, aba):
    new_string = to_check[1] + to_check[0] + to_check[1]
    return new_string == aba


def support_ssl(ip_address):
    list1 = ip_address.split('[')
    list2 = []
    temp_aba = []
    temp_bab = []
    for n in list1:
        if ']' in n:
            temp = n.split(']')
            list2.append(temp[0])
            list2.append(temp[1])
        else:
            list2.append(n)
    for i in range(len(list2)):
        temp_list = get_aba(list2[i])
        if i % 2 == 0 and len(temp_list) != 0:
            for temp in temp_list:
                temp_aba.append(temp)
        elif i % 2 != 0 and len(temp_list) != 0:
            for temp in temp_list:
                temp_bab.append(temp)
    for case in temp_aba:
        for compared in temp_bab:
            if is_bab(case, compared):
                return True
    return False

for line in puzzle_input:
    if support_ssl(line):
        count += 1
print(count)
