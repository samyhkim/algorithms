def compareVersion(version1, version2):
    v1 = helper(version1)
    v2 = helper(version2)
    if v1 > v2:
        return 1
    elif v1 < v2:
        return -1
    else:
        return 0


def helper(v):
    v = list(map(int, v.split(".")))
    # tackle tailing 0 case: 1.0.0 vs 1
    i = len(v)-1
    while i >= 0 and v[i] == 0:
        i -= 1
    return v[:i+1]


print(compareVersion("1", "1.0.1"))
