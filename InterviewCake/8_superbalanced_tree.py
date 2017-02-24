#!/usr/bin/env python

def is_balanced(root):
    if not root: return True

    # Short-circuit as soon as we find >2.
    depths = []

    # Stack that will hold tuples of (node, depth).
    nodes = []
    nodes.append((tree_root, 0))

    while len(nodes):
        node, depth = nodes.pop()

        # Case: we found a leaf.
        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart.
                if ((len(depths) > 2) or
                        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                    return False

        # Case: not a leaf, keep going.
        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True
