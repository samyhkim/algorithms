'''
If we take XOR of zero and some bit, it will return that bit
a ⊕ 0 = a
If we take XOR of two same bits, it will return 0
a ⊕ a = 0
a ⊕ b ⊕ a = ( a ⊕ a ) ⊕ b = 0 ⊕ b = b
So we can XOR all bits together to find the unique number.

a = 0
2: 0 XOR 2 = 2
2: 2 XOR 2 = 0
1: 0 XOR 1 = 1

a = 0
4: 0 XOR 4 = 4
1: 4 XOR 1 = 5
2: 5 XOR 2 = 7
1: 7 XOR 1 = 6
2: 6 XOR 2 = 4
'''


# bit manipulation: O(n), O(1)
def single_number(nums):
    a = 0
    for i in nums:
        a = a ^ i
    return a

# dictionary: O(n), O(n)


def single_number(nums):
    lookup = {}
    for num in nums:
        lookup[num] = lookup.get(num, 0) + 1
    for key, val in lookup.items():
        if val == 1:
            return key


print(single_number([2, 2, 1]) == 1)
print(single_number([4, 1, 2, 1, 2]) == 4)
