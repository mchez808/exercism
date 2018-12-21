# ===================================
# ===================================

# https://exercism.io/my/solutions/44dd9306239f48329c853af2bb9af7df

# see Trello procedural list
# https://trello.com/b/8CsaJ6rv/play

# ===================================
# ===================================

input = "1"
output = [int(input)]
# ASSUMPTION HERE: integers only

#  reading each row left-to-right while moving top-to-bottom across the rows,

# GOAL
output = [[1, 2], [3, 4]]

# example
example = np.array([[1, 2], [3, 4]])
# array([[1, 2],
#        [3, 4]])


# APPROACH
input = "1 2\n3 4"
import re
import numpy as np
list_of_str = re.findall(r'\d', input)
list_of_int = list(map(int, list_of_str))
arr = np.array(list_of_int)
nrow = len(input.split('\n'))
ncol = int(len(list_of_int) / nrow)
arr.shape = nrow, ncol

# what NOT to do:
    # re.sub(' ', ',', input)
    # # We want return a matrix, NOT a string.

    # list_of_rows = input.split('\n')
    # [row.split(' ') for row in list_of_rows]
    # # This results in a matrix of strings!



class Matrix(object):
    def __init__(self, matrix_string):
        pass

    def row(self, index):
        pass

    def column(self, index):
        pass
