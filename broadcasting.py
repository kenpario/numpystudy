import numpy as np

array1 = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
array2 = np.array([8, 9, 10])
array3 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
array4 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

sum = array1 + array2
mul = array1 * array2

print(sum)
print(mul)
print(array3 * array4)
