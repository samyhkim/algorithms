function twoSum(nums, target) {
  let map = new Map();

  for (let i = 0; i < nums.length; i++) {
    matchingPair = target - nums[i];
    if (map.has(matchingPair)) {
      return [map.get(matchingPair), i];
    } else {
      map.set(nums[i], i);
    }
  }
  return [];
}

const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target));
