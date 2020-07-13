'''
put all nums in hash
for each num in hash, check if x + 1 exists, if so count ++
return count

arr = [1,1,3,3,5,5,7,7]
hash = {1, 3, 5, 7}
lookup[num] + 1
'''


def count_elements(arr):
    lookup = {}
    count = 0
    for num in arr:
        lookup[num] = lookup.get(num, 0) + 1
    for num in arr:
        if num + 1 in lookup:
            count += 1
    return count


print(count_elements([1, 1, 3, 3, 5, 5, 7, 7]))
print(count_elements([1, 2, 3]))
print(count_elements([1, 3, 2, 3, 5, 0]))
print(count_elements([1, 1, 2, 2]))
print(count_elements([0, 1]))
