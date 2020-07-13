def letter_combinations(digits):
    if not digits:
        return []
    lookup = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": "_"
    }
    res = []
    dfs(digits, lookup, res, "", 0)
    return res


def dfs(digits, lookup, res, path, index):
    if len(path) == len(digits):
        res.append(path)
        return
    # represents path index
    for i in range(index, len(digits)):  # 2 -> 3
        # represents values of current path index's key
        for letter in lookup[digits[i]]:  # a b c -> d e f
            dfs(digits, lookup, res, path + letter, i + 1)


print(letterCombinations("23"))
