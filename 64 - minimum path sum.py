# def minPathSum(grid):
#     m = len(grid)
#     n = len(grid[0])
#     for i in range(1, n):
#         grid[0][i] += grid[0][i-1]
#     for i in range(1, m):
#         grid[i][0] += grid[i-1][0]
#     for i in range(1, m):
#         for j in range(1, n):
#             grid[i][j] += min(grid[i-1][j], grid[i][j-1])
#     return grid[-1][-1]


def minPathSum(grid):
    for row in range(1, len(grid)):
        grid[row][0] += grid[row-1][0]
    for col in range(1, len(grid[0])):
        grid[0][col] += grid[0][col-1]
    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    return grid[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(minPathSum(grid))
