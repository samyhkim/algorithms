function mergeTwoLists(l1, l2) {
  let l3, curr;
  l3 = curr = { val: 0, next: null };

  while (l1 && l2) {
    if (l1.val <= l2.val) {
      curr.next = l1;
      curr = curr.next;
      l1 = l1.next;
    } else {
      curr.next = l2;
      curr = curr.next;
      l2 = l2.next;
    }
  }
  curr.next = l1 || l2;
  return l3.next;
}

var l1 = {
  value: 1,
  next: {
    value: 2,
    next: {
      value: 4,
      next: null,
    },
  },
};

var l2 = {
  value: 1,
  next: {
    value: 3,
    next: {
      value: 4,
      next: null,
    },
  },
};

console.log(mergeTwoLists(l1, l2));
