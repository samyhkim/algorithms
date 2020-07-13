def is_happy(n):
    seen = {}
    while n not in seen:
        seen[n] = n
        sum_list = []
        for i in str(n):
            sum_list.append(int(i) ** 2)
        n = sum(sum_list)
    return n == 1


# pythonic
# def is_happy(n):
#     seen = set()
#     while n not in seen:
#         seen.add(n)
#         n = sum([int(i)**2 for i in str(n)])
#     return n == 1


print(is_happy(19))
