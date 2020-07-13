'''
We generate a bottom up DP table.

The tricky part is handling the corner cases (e.g. s = "30").

Most elegant way to deal with those error/corner cases, is to allocate an extra space, dp[0].

Let dp[ i ] = the number of ways to parse the string s[1: i + 1]

For example:
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2
'''


def num_decodings(s):
    if not s or s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)

    # base case initialization
    dp[0] = 1
    dp[1] = 1  # (1)

    for i in range(2, len(s) + 1):
        one_step = int(s[i - 1:i])
        two_step = int(s[i - 2:i])
        # One step jump
        if 0 < one_step:  # (2)
            dp[i] = dp[i - 1]
        # Two step jump
        if 10 <= two_step <= 26:  # (3)
            dp[i] += dp[i - 2]

    return dp[-1]


print(num_decodings("2267"))
