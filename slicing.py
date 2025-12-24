import numpy as np

# we need a 2D array to work with
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

# array['slice expression']
# array[start:end:step] there are 3 indeces saparated by the :

# example of the start index
# print(array[0]) # get the first array(row)

# we can select a range, we need both a start&end indeces
print(array[0:2]) # get the 1st two rows (end is exclusive)