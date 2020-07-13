var lengthOfLongestSubstring = function (s) {
  let map = new Map();
  let start = 0;
  let max_length = 0;

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i]) && start <= map.get(s[i])) {
      start = map.get(s[i]) + 1;
    } else {
      max_length = Math.max(max_length, i - start + 1);
    }
    map.set(s[i], i);
  }

  return max_length;
};

console.log(lengthOfLongestSubstring("pwwkew"));
console.log(lengthOfLongestSubstring("dvdf"));
