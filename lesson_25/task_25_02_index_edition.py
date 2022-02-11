def is_palindrome(looking_str: str, index: int = 0):
    if len(looking_str) <= 1:
        return True
    else:
        # if back_index = -(len(looking_str)-1-index)
        back_index = -(len(looking_str)-1-index)
        if looking_str[index] == looking_str[back_index]:
            index += 1
            return is_palindrome(looking_str, index)
        else:
            return False

# нормализация строки - к нижнему регистру привести посимвольно в итерации
# print(is_palindrome('lolaaaaawol'))
# print(is_palindrome('lool'))
# print(is_palindrome('radar'))

str = 'abcdifg'
index = 3
back_index = (len(str)-1-index)
print(str[index])
print(-back_index)
print(str[back_index])

