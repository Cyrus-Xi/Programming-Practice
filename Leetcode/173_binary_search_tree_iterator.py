#!/usr/bin/env python

"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stk = []
        self.push_lefts(root)
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stk)

    def next(self):
        """
        :rtype: int
        """
        x = self.stk.pop()
        self.push_lefts(x.right)
        return x.val
        
    def push_lefts(self, node):
        while node:
            self.stk.append(node)
            node = node.left
