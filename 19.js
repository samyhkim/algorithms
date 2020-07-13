function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : val;
}

function removeNthFromEnd(head, n) {
  let dummy, fast, slow;
  dummy = fast = slow = { val: 0, next: head };

  for (i = 0; i < n; i++) {
    fast = fast.next;
  }

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next;
  }

  slow.next = slow.next.next;

  return dummy.next;
}

var head = {
  value: 1,
  next: {
    value: 2,
    next: {
      value: 3,
      next: {
        value: 4,
        next: null,
      },
    },
  },
};

console.log(removeNthFromEnd(head, 2));
