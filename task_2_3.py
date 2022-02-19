alphabet = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input()
res = ''
for char in s:
    res += alphabet[(alphabet.index(char) + n) % len(alphabet)]
print('Result: "' + res + '"')