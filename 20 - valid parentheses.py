'''
iterate through string and check in lookup
if key does not exist, add to stack
else, pop from stack and check if it matches with key's value
'''


def is_valid(s):
    open_parens = []
    lookup = {')': '(', ']': '[', '}': '{'}

    for paren in s:
        # only adds opening paren to stack
        if paren not in lookup:
            open_parens.append(paren)
        else:
            # stack == [] catches lone closing paren while stack is empty, like s="]"
            if not open_parens or lookup[paren] != open_parens.pop():
                return False

    # will catch lone opening paren, like s="["
    return open_parens == 0


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
print(is_valid("["))
print(is_valid("]"))
print(is_valid(""))
