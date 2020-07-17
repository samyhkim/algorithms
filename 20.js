function isValid(s) {
  const stack = [];
  const parens = new Map();

  parens.set(")", "(");
  parens.set("]", "[");
  parens.set("}", "{");

  for (let i = 0; i < s.length; i++) {
    if (!parens.has(s[i])) {
      stack.push(s[i]);
    } else {
      if (stack.length === 0 || stack.pop() !== parens.get(s[i])) {
        return false;
      }
    }
  }

  return stack.length === 0;
}

console.log(isValid("()"));
console.log(isValid("()[]"));
console.log(isValid("(])]"));
console.log(isValid("("));
console.log(isValid(")"));
