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

# 4- 3D array (beyonf imagination)
matrix3D = np.array(
    [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],
     [[10, 11, 12],[13, 14, 15],[16, 17, 18]],
     [[19, 20, 21],[22, 23, 24],[25, 26, 27]]] 
)

print(f"Dimenions: {matrix3D.ndim}")
print(matrix3D)


# ! key lesson: a n-D array is basically an array of (n-1D) arrays