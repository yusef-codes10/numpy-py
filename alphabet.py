import numpy as np

alphabet = np.array([
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
    [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
    [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', ' ']]   
])

print(alphabet)

# we are going to concatneate a word from that array
# string concatenation is simply addig strings
word = alphabet[2, 2, 0] + alphabet[2, 0, 2] + alphabet[2, 0, 0] + alphabet[0, 1, 1] + alphabet[0, 1, 2]
print(word)

# explain the length & R
# 1- scalar, belongs to R
print(alphabet[0][0][0])

# 2- 1D array, belongs to ℝⁿ n is the length (in this case 3)
print(alphabet[0][0])

# 3- 2D array (Matric), belongs to ℝⁿᵐ
print(alphabet[0])

# ! A dimension is the number of indeces needed to reach a scalar
