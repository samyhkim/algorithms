def combination(nums, target):
    combinations = []
    nums.sort()  # sort first so dfs break condition is possible
    dfs(nums, target, combinations, [], 0)
    return combinations


def dfs(nums, target, combinations, path, nums_idx):
    if target == 0:
        combinations.append(path)
        return

    for i in range(nums_idx, len(nums)):
        # allows us to check before starting new dfs path
        # also increases nums_idx when condition is met
        if target < nums[i]:
            break

        # i prevents infinite loop
        # i does not change so we can try every element from the beginning of nums with each dfs path
        # candidates = [2, 3], target = 6; path = [2, 2, 2]
        dfs(nums, target - nums[i], combinations, path + [nums[i]], i)


candidates = [2, 3, 6, 7]
target = 7

print(combination(candidates, target))
