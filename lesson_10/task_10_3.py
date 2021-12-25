# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

my_list = [(i, j) for i in range(0, 4, 1) for j in range(i ** 2)]
print(my_list)
