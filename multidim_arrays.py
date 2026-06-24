import numpy as np

# array = np.array(['A', 'B', 'C'])
# array = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
array = np.array(
    [[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]])

print(array.ndim)
print(array.shape)
print(array[0][0][0])
print(array[0, 0, 0])
print(array[1, 2, 1])
word = array[0, 1, 0] + array[1, 1, 2] + array[0, 2, 0]
print(word)
