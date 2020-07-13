def is_anagram(s, t):
    s_lookup = {}
    t_lookup = {}
    for i in s:
        s_lookup[i] = s_lookup.get(i, 0) + 1
    for i in t:
        t_lookup[i] = t_lookup.get(i, 0) + 1
    return s_lookup == t_lookup


# one dictionary
def is_anagram(s, t):
    lookup = {}
    for i in s:
        lookup[i] = lookup.get(i, 0) + 1
    for i in t:
        if i not in lookup:
            return False
        else:
            lookup[i] -= 1
    for val in lookup.values():
        if val != 0:
            return False
    return True


print(is_anagram("anagram", "nagaram"))
