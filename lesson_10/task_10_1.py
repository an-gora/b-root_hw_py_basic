# Make a program that has some sentence (a string) on input and
# returns a dict containing all unique words as keys and
# the number of occurrences as values.

def unique_dictionary() -> dict:
    sentence = input('write some sentence: ')
    list_of_words = sentence.split(' ')
    unique_set = list(set(list_of_words))
    my_dict = dict()
    counter = 0
    for word in unique_set:
        counter = list_of_words.count(word)
        my_dict.update({word: counter})
    return my_dict


if __name__ == '__main__':
    print(unique_dictionary())

# very very new new tree
