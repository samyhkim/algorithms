def numRookCaptures(board):
    moves = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                x = i
                y = j
                break
    for i, j in ([1, 0], [-1, 0], [0, 1], [0, -1]):
        row = x + i
        col = y + j
        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'p':
                moves += 1
            if board[row][col] != '.':  # board[r][c] == 'B' will count all p's
                break
            row += i
            col += j
    return moves


board = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]

print(numRookCaptures(board))
