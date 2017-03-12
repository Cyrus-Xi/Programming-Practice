#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
 
def reverse_ll(head):
    curr, prev = head, None
    while curr:
        curr.next, prev, curr = prev, curr,  curr.next
    return prev

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c

r = reverse_ll(a)
assert r.value == 3
assert r.next.value == 2
assert r.next.next.value == 1
assert not r.next.next.next

# Edge cases: empty linked list and single node linked list.
assert not reverse_ll(None)
assert reverse_ll(LinkedListNode(5)).value == 5
print 'Tests passed!'
