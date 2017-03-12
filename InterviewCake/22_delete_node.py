#!/usr/bin/env python

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def delete_node(node):
    if not node: return None
    if not node.next: raise Exception("Can't delete the last node.")
    node.value = node.next.value
    node.next = node.next.next
    return node
