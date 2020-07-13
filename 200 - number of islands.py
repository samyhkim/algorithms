def num_islands(grid):
    if not grid:
        return 0

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count


def dfs(grid, row, col):
    if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
        return

    if grid[row][col] != "1":
        return

    grid[row][col] = "#"  # backtracking, prevent re-count

    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        dfs(grid, row + i, col + j)


grid = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "1"]]

print(num_islands(grid))
