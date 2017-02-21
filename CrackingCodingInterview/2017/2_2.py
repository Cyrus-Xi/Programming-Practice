#!/usr/bin/env python

from linkedlist import Node

# Naive, do 2 passes.
def kth_to_last(head, k):
    curr = head
    kth = curr
    length = 0

    while curr:
        curr = curr.next_node
        length += 1

    # Can't return kth.
    if length < k: return -1

    up_to = length - 1 - (k - 1)
    for i in xrange(up_to):
        kth = kth.next_node

    return kth.data

# Do it in 1 pass.
def kth_to_last2(head, k):
    curr = head
    runner = head

    # Separate the pointers by k-1.
    for i in xrange(k-1):
        runner = runner.next_node
        # Went off the edge: list isn't long enough.
        if not runner: return -1
    
    # When runner goes off the end, we know curr is the kth node from the end.
    while runner:
        curr = curr.next_node
        runner = runner.next_node

    return curr.data


t1 = Node('a')
t1.next_node = Node('b')
t1.next_node.next_node = Node('c')

t1b = Node('a')
t1b.next_node = Node('b')
t1b.next_node.next_node = Node('c')

print kth_to_last(t1, 2)
print "should be b"

print kth_to_last(t1b, 2)
print "one pass, should be b"

t2 = Node('a')
t2.next_node = Node('b')
t2.next_node.next_node = Node('c')
t2.next_node.next_node.next_node = Node('d')
t2.next_node.next_node.next_node.next_node = Node('e')

t2b = Node('a')
t2b.next_node = Node('b')
t2b.next_node.next_node = Node('c')
t2b.next_node.next_node.next_node = Node('d')
t2b.next_node.next_node.next_node.next_node = Node('e')

print kth_to_last(t2, 3)
print "should be c"

print kth_to_last(t2b, 3)
print "one pass, should be c"
