# end = '\n' means empty line
# expected output - hello + 2 empties lines
print('hello', end='\n\n')

# sep = 'specific symbol' - add separator between entities in print
# expected output - a*b*c
print('a', 'b', 'c', sep='*')

# expected output - hi there@
print('hi there', end=' @')

# expected output - Hhi there    hi
print('hi there', end='\t')
print('hi')

# expected output - a*b*c@
print('a', 'b', 'c', sep='*', end='@')