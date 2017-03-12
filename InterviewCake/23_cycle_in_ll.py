#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
        
def is_cycle(root):
    if not root.next: return True
    c1, c2 = root, root.next
    while c2 and c2.next:
        if c1 == c2: return True
        c1, c2 = c1.next, c2.next.next
    return False

