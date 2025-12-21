import numpy as np

# this is a 0 dimensional array (single value)
array = np.array('!')

# number of dimension using the ndim property

print(f"Dimenions: {array.ndim}")
print(array)

# 2- this is 1 dimensional array (1 row)
vector = np.array([1, 2, 3, 4])

print(f"Dimenions: {vector.ndim}")
print(vector)