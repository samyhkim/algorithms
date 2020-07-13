def min_knight_moves(x, y):
    memo = {}
    return dfs(abs(x), abs(y), memo)


def dfs(x, y, memo):
    if (x, y) not in memo:
        if x + y == 0:
            return 0
        if x + y == 2:
            return 2
        # +1 to count this current function call
        min_moves = min(dfs(abs(x - 1), abs(y - 2), memo),
                        dfs(abs(x - 2), abs(y - 1), memo)) + 1
        memo[(x, y)] = min_moves
    return memo[(x, y)]


print(min_knight_moves(2, 1))

# def min_knight_moves(x, y):
#     def dfs(x, y):
#         if (x, y) not in memo:
#             x, y = abs(x), abs(y)
#             if x == y == 0:
#                 return 0
#             if x + y == 2:
#                 return 2
#             ans = min(dfs(x - 1, y - 2), dfs(x - 2, y - 1)) + 1
#             memo[(x, y)] = ans
#         return memo[(x, y)]
#     memo = {}
#     return dfs(x, y)
