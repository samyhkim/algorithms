# Follow up: solve in O(n), O(1)


def backspace_compare(s, t):
    l1 = stack(s, [])
    l2 = stack(t, [])
    return l1 == l2


def stack(s, stack):
    for char in s:
        if char is not "#":
            stack.append(char)
        else:
            if not stack:
                continue
            stack.pop()
    return stack


print(backspace_compare("ab#c", "ad#c") == True)
print(backspace_compare("a##c", "#a#c") == True)
print(backspace_compare("a#c", "b") == False)
