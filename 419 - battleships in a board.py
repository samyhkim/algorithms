'''
Brute force:
DFS like "200 - Number of Islands"

Time: ?
Space: ?

Optimized:
Utilize a flag to represent if if it the first time we are seeing "X", or
if it has been counted before.

Since we are moving from left to right and top to bottom, if a coordinate
above or left to us have an "X", then we must have counted it already, so
set flag to 0.

If we haven't seen this "X" before, add it to the total battleships count.

Time: O(mn)
Space: O(1)
'''


def count_battleships(board):
    battleships = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                flag = 1
                if col > 0 and board[row][col-1] == 'X':  # check left
                    flag = 0
                if row > 0 and board[row-1][col] == 'X':  # check below
                    flag = 0

                battleships += flag

    return battleships


def count_battleships(board):
    battleships = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "X":
                dfs(board, row, col)
                battleships += 1

    return battleships


def dfs(board, row, col):
    if not 0 <= row < len(board) or not 0 <= col < len(board[0]):
        return

    if board[row][col] != "X":
        return

    board[row][col] = "#"  # backtracking, prevent re-count

    for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        dfs(board, row + i, col + j)


grid = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
print(count_battleships(grid))
