#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def kth_to_last_node(k, head):
    prev, curr = head, head
      # Move curr k-1 nodes ahead of head/prev.
    for _ in xrange(k - 1):
        if not curr.next: raise Exception("List is too short to get the kth to last node.")
        curr = curr.next
    # Not `while curr` since then would go one node too far.
    while curr.next:
        prev, curr = prev.next, curr.next
    return prev
        
a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

assert kth_to_last_node(3, a).value == 'Cheese'
print 'Test passed!'
