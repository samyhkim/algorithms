def find_strobogrammatic(n):
    strobogrammatic = []
    lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    helper(strobogrammatic, lookup, [None] * n, 0, n - 1)
    return strobogrammatic


def helper(strobogrammatic, lookup, item, start, end):
    if start > end:
        strobogrammatic.append(''.join(item))
        return

    for key in lookup:
        if start == end and key in ('6', '9'):
            continue
        if start != end and start == 0 and key == '0':
            continue

        item[start] = key
        item[end] = lookup[key]

        helper(strobogrammatic, lookup, item, start+1, end-1)


print(find_strobogrammatic(2))
