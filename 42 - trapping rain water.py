def trap(height):
    if height is None or len(height) < 3:
        return
    volume = 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        # subtract current height from max height
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
