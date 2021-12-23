# Write a Python program to get a string made of
# the first 2 and the last 2 chars from a given string.
# If the string length is less than 2,
# return instead of the empty string.

def work_with_given_string(data: str) -> str:
    result_string = ''
    if len(data) >= 2:
        result_string = ''.join([data[0:2], data[-2:]])
    return result_string


if __name__ == '__main__':
    print(work_with_given_string('my'))
