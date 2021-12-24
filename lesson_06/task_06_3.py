# Write a program that has a variable with
# your name stored (in lowercase) and then asks
# for your name as input. The program should check
# if your input is equal to the stored name even
# if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”,
# it should return True.

def is_name_same() -> bool:
    stored_name = 'staci'
    input_name = input('please insert name: ').lower()
    if stored_name == input_name:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_name_same())
