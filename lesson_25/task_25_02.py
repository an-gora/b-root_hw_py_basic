def is_palindrome(looking_str: str):
    if len(looking_str) <=1:
        return True
    else:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1:-1])
        else:
            return False

print(is_palindrome('lolaaaaawol'))
print(is_palindrome('lool'))
print(is_palindrome('radar'))
