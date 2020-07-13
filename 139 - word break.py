def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        # dp[i] checks if left side of the string has already been found
        # if so, continue checking the right side of the string
        if dp[i] == True:
            for j in range(i + 1, len(s)+1):
                if s[i:j] in wordDict:
                    dp[j] = True
    return dp[-1]


s = "leetcode"
wordDict = ["leet", "code"]
print(word_break(s, wordDict))
