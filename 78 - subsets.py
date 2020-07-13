def subsets(nums):
    res = []
    dfs(nums, res, [], 0)
    return res


def dfs(nums, res, path, index):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, res, path+[nums[i]], i+1)


print(subsets([1, 2, 3]))
