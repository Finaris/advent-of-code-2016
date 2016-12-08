import hashlib

input_string = 'ojvtpuvg'
password = ''
index = 0

while len(password) < 8:
    temp_string = input_string + str(index)
    swag = hashlib.md5(temp_string.encode('utf-8')).hexdigest()
    if swag[:5] == '00000':
        password += swag[5]
    index += 1

print(password)
