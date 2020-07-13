def decode_string(s):
    stack = []
    cur_num = 0
    cur_string = ''
    for c in s:
        if c == '[':
            stack.append(cur_string)
            stack.append(cur_num)
            cur_string = ''
            cur_num = 0
        elif c == ']':
            num = stack.pop()
            prev_string = stack.pop()
            cur_string = prev_string + (num * cur_string)
        elif c.isdigit():
            cur_num = cur_num * 10 + int(c)
        else:
            cur_string += c
    return cur_string


print(decode_string("3[a]2[bc]") == "aaabcbc")
print(decode_string("3[a2[c]]") == "accaccacc")
print(decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef")
