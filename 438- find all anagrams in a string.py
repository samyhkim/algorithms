from collections import Counter


def find_anagrams(s, p):
    output = []
    p_lookup = Counter(p)
    s_lookup = Counter(s[:len(p)])
    left = 0
    right = len(p)

    while right <= len(s):  # can come down to last comparison

        if s_lookup == p_lookup:
            output.append(left)

        s_lookup[s[left]] -= 1
        if s_lookup[s[left]] == 0:
            s_lookup.pop(s[left])

        if right < len(s):  # index will be out of range in last comparison
            s_lookup[s[right]] += 1

        left += 1
        right += 1

    return output


print(find_anagrams("cbaebabacd", "abc"))
