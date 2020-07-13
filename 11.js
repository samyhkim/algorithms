function maxArea(heights) {
  let left = 0;
  let right = heights.length - 1;
  let max_area = 0;

  while (left < right) {
    let area = Math.min(heights[left], heights[right]) * (right - left);
    max_area = Math.max(max_area, area);

    if (heights[left] < heights[right]) {
      left += 1;
    } else {
      right -= 1;
    }
  }

  return max_area;
}

let heights = [1, 8, 6, 2, 5, 4, 8, 3, 7];
console.log(maxArea(heights));
