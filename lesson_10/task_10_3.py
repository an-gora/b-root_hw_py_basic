# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

def main():
    my_list = [(i, i ** 2) for i in range(0, 4, 1)]
    return my_list


# my_list = [(i,j) for i,j in range(0, 4, 1)]
if __name__ == '__main__':
    print(main())
