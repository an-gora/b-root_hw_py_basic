# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible
# by 7 but not a multiple of 5, and store them in a separate list.
# Finally, print the list.
# Constraint: use only while loop for iteration

def extracting_numbers() -> list[int]:
    all_integer_list = list(range(1, 100, 1))
    range_len = len(all_integer_list)
    separate_list = []
    i = 0
    while i < range_len:
        if (all_integer_list[i]) % 7 == 0 and (all_integer_list[i]) % 5 != 0:
            separate_list.append(all_integer_list[i])
        i += 1
    return separate_list


if __name__ == '__main__':
    print(extracting_numbers())
