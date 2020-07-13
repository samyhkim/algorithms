def max_area(height):
    max_area = 0

    left = 0
    right = len(height) - 1
    while left < right:
        # height * width
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)

        # always want to find greatest height for max area possible
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
