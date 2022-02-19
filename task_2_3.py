# alphabet = ' abcdefghijklmnopqrstuvwxyz'
# n = int(input())
# s = input()
# res = ''
# for char in s:
#     res += alphabet[(alphabet.index(char) + n) % len(alphabet)]
# print('Result: "' + res + '"')
import string

alphabet_string = string.ascii_lowercase
print(alphabet_string)

key = '5'
data_for = 'tea'
data = f'{key} {data_for}'
print(data)

key, data_for_cipher = data.split(' ', 1)
print(key)
print(data_for_cipher)