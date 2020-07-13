'''
Test case: "123", "456"

Brute force:
Nested for loops to multiply each number against each other.
End of nested loops result in [[837, 516, 294]]. Add these together
with another nested loop.

Optimized:

'''


def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))

    for i, n1 in enumerate(reversed(num1)):
        for j, n2 in enumerate(reversed(num2)):
            product[i + j] += int(n1) * int(n2)
            product[i + j + 1] += product[i + j] // 10
            product[i + j] %= 10

    while len(product) > 1 and product[-1] == 0:
        product.pop()

    return "".join([str(i) for i in reversed(product)])

# def multiply(num1, num2):
#     res = []
#     prod = 1
#     num1 = list(num1)
#     num2 = list(num2)
#     for i in reversed(num2):
#         carry = 0
#         for j in reversed(num1):
#             n1 = ord(i) - ord('0') if num1 else 1
#             n2 = ord(j) - ord('0') if num2 else 1
#             prod = n1 * n2
#             res.append(str(carry + prod % 10))
#             carry = prod // 10
#         "".join(res)

#     return res


print(multiply('123', '456'))
