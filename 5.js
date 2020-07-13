function longestPalindrome(s) {
  let max_palindrome = "";

  for (let i = 0; i < s.length; i++) {
    let type1 = palindromeCheck(s, i, i);
    if (type1.length > max_palindrome.length) {
      max_palindrome = type1;
    }

    let type2 = palindromeCheck(s, i, i + 1);
    if (type2.length > max_palindrome.length) {
      max_palindrome = type2;
    }
  }

  return max_palindrome;
}

function palindromeCheck(s, left, right) {
  while (0 <= left && right < s.length && s[left] === s[right]) {
    left -= 1;
    right += 1;
  }

  return s.slice(left + 1, right);
}

console.log(longestPalindrome("babad"));
console.log(longestPalindrome("cbbd"));
