#!/usr/bin/env

from linkedlist import Node

def remove_dupes(head):
    # Edge case where single node list.
    if not head.next_node: return head

    curr, prev = head, Node()
    dupes = {}
    
    while curr:
        if curr.data in dupes:
            prev.next_node = curr.next_node
        else:
            dupes[curr.data] = 1
            prev = curr

        curr = curr.next_node

# Now do it without another data structure.
def remove_dupes2(head):
    if not head.next_node: return head

    curr, runner = head, head.next_node

    while curr:
        runner = curr
        while runner.next_node:
            if curr.data == runner.next_node.data:
                runner.next_node = runner.next_node.next_node
            else:    
                runner = runner.next_node
        curr = curr.next_node
            

# a, a, b | a, b, b, a
t1 = Node('a')
t1.next_node = Node('a')
t1.next_node.next_node = Node('b')

t11 = Node('a')
t11.next_node = Node('a')
t11.next_node.next_node = Node('b')

t2 = Node('a')
t2.next_node = Node('b')
t2.next_node.next_node = Node('b')
t2.next_node.next_node.next_node = Node('a')

t21 = Node('a')
t21.next_node = Node('b')
t21.next_node.next_node = Node('b')
t21.next_node.next_node.next_node = Node('a')
t21.next_node.next_node.next_node.next_node = Node('a')

remove_dupes(t1)
remove_dupes(t2)

while t1:
    print t1.data
    t1 = t1.next_node

while t2:
    print t2.data
    t2 = t2.next_node

remove_dupes(t11)
remove_dupes(t21)

while t11:
    print t11.data
    t11 = t11.next_node

while t21:
    print t21.data
    t21 = t21.next_node

