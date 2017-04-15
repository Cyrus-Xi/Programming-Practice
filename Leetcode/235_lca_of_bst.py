#!/usr/bin/env python

def lowestCommonAncestor(self, root, p, q):
    if not root or not p or not q: return None
    if max(p.val, q.val) < root.val: 
        return self.lowestCommonAncestor(root.left, p, q)
    if min(p.val, q.val) > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root
