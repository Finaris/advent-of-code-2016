input_text = open('input.txt', 'r')
rooms = [line.strip() for line in input_text]


def get_shifted_letter(letter_to_shift, shift_num):
    new_char = ord(letter_to_shift) + (shift_num % 26)
    if new_char > 122:
        new_char -= 26
    elif new_char < 97:
        new_char += 26
    return chr(new_char)

for room in rooms:
    room_string = (room.replace('-', '')).partition("[")[0]
    room_compare = room.partition("[")[-1]
    room_compare = room_compare[0:len(room_compare)-1]
    index = room.index('[')
    sector_id = (room[index-1:index-4:-1])[::-1]
    dictionary = {}
    for n in room_compare:
        dictionary[n] = 0
    for n in room_string:
        if n in dictionary:
            dictionary[n] += 1
    sort_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    temp = 0
    shift = 0
    new_thing = ''
    for n in sort_dict:
        char = n[0]
        count = n[1]
        if count == 0:
            continue
        elif count < temp:  #
            shift = 0
            new_thing = new_thing + char
        elif count > temp:
            shift = 0
            new_thing = char + new_thing
        else:
            temp_char = new_thing[len(new_thing)-1-shift:len(new_thing)] + char
            temp_string = ''
            for o in sorted(temp_char):
                temp_string = temp_string + o
            new_thing = new_thing[0:len(new_thing)-1-shift] + temp_string
        if temp == count:
            shift += 1
        temp = count
    if room_compare == new_thing:
        new_room_string = room.partition("[")[0]
        new_room_string = new_room_string[0:len(new_room_string)-4]
        new_room_strings = new_room_string.split('-')
        temp_strings = [0 for i in range(len(new_room_strings))]
        count = 0
        for m in new_room_strings:
            shifted_string = ''
            for n in m:
                shifted_string += get_shifted_letter(n, int(sector_id))
            temp_strings[count] = shifted_string
            count += 1
        if 'object' in temp_strings:
            print(temp_strings, sector_id)
