def strStr(haystack, needle):
    '''
    rtype: int - the index of where needle exists
    '''
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))
