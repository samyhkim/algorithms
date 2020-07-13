def first_unique(s):
    lookup = {}
    for i in range(len(s)):
        if s[i] not in lookup:
            lookup[s[i]] = [i, 1]
        else:
            lookup[s[i]][1] += 1
    for i in lookup:
        if lookup[i][1] == 1:
            return lookup[i][0]


print(firstUnique("loveleetcode"))
