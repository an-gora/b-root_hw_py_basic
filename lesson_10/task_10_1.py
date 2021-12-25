# Make a program that has some sentence (a string) on input and
# returns a dict containing all unique words as keys and
# the number of occurrences as values.

def unique_dictionary() -> dict:
    sentence = input('write some sentence: ')
    list_of_words = sentence.split(' ')
    my_dict = {}
    unique_set = set(list_of_words)

    return unique_set


if __name__ == '__main__':
    print(unique_dictionary())
