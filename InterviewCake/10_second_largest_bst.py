#!/usr/bin/env python

def get_largest_bst(root):
    if not root: return None
    
    curr = root
    while curr:
        if not curr.right: return curr.value
        else: curr = curr.right

def get_second_largest_bst(root):
    if not root or not curr.left and not curr.right: return None
    
    curr = root
    while curr:
        if curr.left and not curr.right:
            return get_largest_bst(curr.left)
           elif curr.right and not curr.right.left and not curr.right.right:
            return curr.value
        curr = curr.right
    return None
