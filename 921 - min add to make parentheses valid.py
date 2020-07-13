'''
Both approaches:
1. If we encounter an opening paren, set it aside in a stack until we find a matching closing paren.
2. If we encounter a closing paren, check to see that there is a matching opening paren in the stack.
    If so, remove the opening paren from the stack.
    If not, we have encountered a lone closing paren. Count it.
3. The lone opening parens are in the stack at the end of the loop. Count the leftover opening parens
   and the leftover closing parens.

Brute force - O(n), O(n)
Use a stack.

Optimized - O(n), O(1)
Use counters.
'''


def min_add_to_make_valid(S):
    opening_paren = 0
    closing_paren = 0

    for paren in S:
        if paren == "(":
            opening_paren += 1
        else:
            if opening_paren == 0:  # encountered lone ")"
                closing_paren += 1
            else:
                opening_paren -= 1  # found a match

    # contains leftover opening paren and closing paren that don't have matches
    return opening_paren + closing_paren


def brute_force(S):
    count = 0
    stack = []

    for paren in S:
        if paren == "(":
            stack.append(paren)
        if paren == ")":
            if not stack:  # encountered lone ")"
                count += 1
            else:
                stack.pop()  # found a match

    # while stack:
    #     stack.pop()
    #     count += 1
    count += len(stack)

    # contains leftover opening paren and closing paren that don't have matches
    return count
