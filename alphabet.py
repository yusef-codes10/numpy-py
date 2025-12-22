import numpy as np

alphabet = np.array([
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
    [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
    [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', ' ']]   
])

print(alphabet)

# we are going to concatneate a word from that array
# string concatenation is simply addig strings
word = alphabet[0, 0, 0]
print(word)