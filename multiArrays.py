import numpy as np

# 1- this is a 0 dimensional array (single value)
array = np.array('!')

# number of dimension using the ndim property

print(f"Dimenions: {array.ndim}")
print(array)

# 2- this is 1 dimensional array (1 row)
vector = np.array([1, 2, 3, 4])

print(f"Dimenions: {vector.ndim}")
print(vector)

# 3- this a 2D array (Matrix)
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(f"Dimenions: {matrix.ndim}")
print(matrix)
