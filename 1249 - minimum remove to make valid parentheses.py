def min_to_remove(s):
    curr = ""
    stack = []

    for char in s:
        # save everything encountered so far and reset curr
        if char == "(":
            stack.append(curr)
            curr = ""
        # close curr substring with parens
        elif char == ")":
            if stack:  # if not stack, then encountered lone closing paren
                curr = stack.pop() + "(" + curr + ")"
        else:
            curr += char

    # get leftover chars - consider test case "())()((("
    # expects "()()" but returns "" without condition
    while stack:
        curr = stack.pop() + curr

    return curr


print(min_to_remove("())()(((("))
