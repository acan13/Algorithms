def rotate(matrix):
    N = len(matrix)
    new_matrix = [[ [] for x in xrange(N)] for x in xrange(N)]
    for row in xrange(N):
        for col in xrange(N):
            new_matrix[col][N - 1 - row] = matrix[row][col]
    return new_matrix

matrix1 = [['a','b','c'],['d','e','f'],['g','h','i']]

print rotate(matrix1)

# def rotate_in_place2(matrix):
#     N = len(matrix)
#
#     for x in xrange(int(N/2)):
#         row = x
#         col = x
#         new_row = x
#         new_col = N - 1 - x
#         temp = matrix[row][col]
#
#         while new_row != x and new_col != x:
#             new_temp = matrix[new_row][new_col]
#             matrix[new_row][new_col] = temp
#             temp = new_temp
#             row = new_row
#             col = new_col
#             new_row = col
#             new_col = N - 1 - row
#     return matrix
#
# print rotate_in_place2(matrix1)

def rotate_in_place3(matrix):
    N = len(matrix)

    for x in xrange(int(N/2)):
        print 'x',x
        temp = matrix[x][:] # top to temp
        print 'temp',temp
        matrix[x] = matrix[:][x] # left to top
        print 'left',matrix[:][0]
        matrix[:][x] = matrix[N-1-x][:] # bottom to left
        matrix[N-1-x][:] = matrix[:][N-1-x] # right to bottom
        matrix[:][N-1-x] = temp # temp to right

    return matrix

print rotate_in_place3(matrix1)
