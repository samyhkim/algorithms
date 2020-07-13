def generate_parentheses(n):
    if not n:
        return []
    res = []
    dfs(n, n, "", res)
    return res


def dfs(left, right, path, res):
    # left (stack of ")") must be larger than right (stack of "(")
    # if not, it creates string like "())"
    if left > right or left < 0 or right < 0:
        return  # backtracking
    if right == 0:
        res.append(path)
        return
    dfs(left - 1, right, path + "(", res)
    dfs(left, right - 1, path + ")", res)


n = 3
output = [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

print(generateParenthesis(n) == output)

'''
dfs(2, 2, [], "")
        dfs(1, 2, [], "(")
                dfs(0, 2, [], "((")
                        dfs(0, 1, [], "(()")
                                dfs(0, 0, [], "(())") # We got "(())" and we append it to ans
                dfs(1, 1, ["(())"], "()")
                        dfs(0, 1, ["(())"], "()(")
                                dfs(0, 0, ["(())"], "()()") # We got "(())" and we append it to ans
                        dfs(1, 0, ["(())", "()()"], "())") # will just return as right < left
        dfs(2, 1, ["(())", "()()"], ")") # will just return as right < left
'''
