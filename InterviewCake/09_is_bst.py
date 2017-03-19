#!/usr/bin/env python

def is_bst(root, high=float('inf'), low=float('-inf')):
    if not root: return True
    if value > high or value < low: return False
    return (is_bst(node.left, high=root.value, low=low) 
            and is_bst(node.right, high=high, low=root.value))
