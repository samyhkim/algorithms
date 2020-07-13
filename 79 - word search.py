def exist(board, word):
    if not board:
        return None

    # have to dfs every letter bc there are duplicates in the board
    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(board, word, row, col):
                return True

    return False


def dfs(board, word, row, col):
    if len(word) == 0:
        return True

    if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or word[0] != board[row][col]:
        return False

    temp = board[row][col]
    board[row][col] = '#'  # prevent backtrack
    res = dfs(board, word[1:], row + 1, col) or dfs(board, word[1:], row - 1, col) \
        or dfs(board, word[1:], row, col + 1) or dfs(board, word[1:], row, col - 1)
    board[row][col] = temp  # put back original value

    return res


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print(exist(board, "ABCCED"))
print(exist(board, "SEE"))
