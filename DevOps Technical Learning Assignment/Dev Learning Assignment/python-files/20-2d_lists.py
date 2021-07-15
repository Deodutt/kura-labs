# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# # 3x3 matrix in math

# # we can model it in python using a 2d list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# matrix[0] #this returns another list
# matrix[0][1] # the second [1] is the index of the first list.

# print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)