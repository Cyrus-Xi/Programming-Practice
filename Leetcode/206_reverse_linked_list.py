#!/usr/bin/env python

# Recursive.
def reverseList(self, head, prev=None):
    if not head: return prev
    # Reverse links, making sure to hold on to the next node.
    curr = head.next
    head.next = prev
    return self.reverseList(curr, head)

# Iterative.
def reverseList(self, head):
    if not head: return
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev
