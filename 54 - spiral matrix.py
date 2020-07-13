def spiral_order(matrix):
    if matrix == []:
        return matrix

    spiral = []

    l = 0
    r = len(matrix[0]) - 1
    t = 0
    b = len(matrix) - 1
    while l < r and t < b:
        for i in range(l, r):  # top
            spiral.append(matrix[t][i])
        for i in range(t, b):  # right
            spiral.append(matrix[i][r])
        for i in reversed(range(r, l)):  # bottom
            spiral.append(matrix[b][i])
        for i in reversed(range(b, t)):  # left
            spiral.append(matrix[i][l])

        l += 1
        r -= 1
        t += 1
        b -= 1

    if l == r and t == b:  # single square
        spiral.append(matrix[t][l])
    elif l == r:  # vertical line
        for i in range(t, b + 1):
            spiral.append(matrix[i][l])
    elif t == b:  # horizontal line
        for i in range(l, r + 1):
            spiral.append(matrix[t][i])

    return spiral


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_order(matrix))
