import hashlib

input_string = 'ojvtpuvg'
password = ['g' for i in range(8)]
index = 0
count = 0

while count < 8:
    temp_string = input_string + str(index)
    swag = hashlib.md5(temp_string.encode('utf-8')).hexdigest()
    if swag[:5] == '00000':
        if 47 < ord(swag[5]) < 56:
            if password[ord(swag[5])-48] == 'g':
                password[ord(swag[5])-48] = swag[6]
                count += 1
    index += 1

[print(x, end='') for x in password]
