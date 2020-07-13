def length_of_longest_substring(s):
    max_length = 0

    visited = {}
    start = 0
    for idx, char in enumerate(s):
        # found a starting point of a new substring
        if char in visited and start <= visited[char]:
            # update start of string index to the next index
            start = visited[char] + 1  # +1 bc zero indexed
        else:
            # check length from start of string to index
            max_length = max(max_length, idx - start + 1)  # +1 bc zero indexed

        # add/update char to/of dictionary
        visited[char] = idx

    return max_length


print(length_of_longest_substring("aab"))
print(length_of_longest_substring(""))
print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))
print(length_of_longest_substring("dvdf"))
