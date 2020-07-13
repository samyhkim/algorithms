# O(n^2) - not sure if optimal; other solutions are O(n) but use zip() and enum()
def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""
    lens = [len(s) for s in strs]
    min_len = min(lens)
    res = ""
    for i in range(1, min_len + 1):
        prefix = strs[0][:i]
        for s in strs:
            if s[:1] != prefix:
                return prefix
            res = prefix
    return res


strs = ['flower', 'flow', 'flight']

print(longestCommonPrefix(strs))
