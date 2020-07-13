def rotate(matrix):
    '''
    rotate 90: reverse and transpose
    '''
    # same as matrix.reverse()
    n = len(matrix)
    for i in range(n // 2):
        matrix[i], matrix[(n-1)-i] = matrix[(n-1)-i], matrix[i]

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output_matrix1 = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
output_matrix2 = [
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
]

print(rotate(matrix1))
# print(rotate(matrix2) == output_matrix2)
