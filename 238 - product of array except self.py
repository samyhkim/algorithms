def product_except_self(nums):
    products = []
    left = 1
    right = 1

    for i in range(len(nums)):
        products.append(left)
        left *= nums[i]

    for i in reversed(range(len(nums))):
        products[i] *= right
        right *= nums[i]

    return products


print(product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6])
