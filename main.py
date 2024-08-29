def morsecode(mess):
    with open('alphabet.txt', 'r', encoding='utf-8') as file:
        x = {y.split(' ', 1)[0]: y.split(" ", 1)[1].strip('\n') for y in file.readlines()}
        print(x)
        morse_mess = ''
    for letter in mess.split():
        morse_mess += x.get(letter, '') + ' '

    return morse_mess
#     pass
#
#
message = input('What would you like to say?').upper()
print(message)
print(morsecode(message))
