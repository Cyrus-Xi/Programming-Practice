#!/usr/bin/env python

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

def addTwoNumbers(self, l1, l2):
    l1_str = ''
    l2_str = ''
        
    while l1.next != None:
        l1_str += str(l1.val)
        l1 = l1.next
    l1_str += str(l1.val)
        
    while l2.next != None:
        l2_str += str(l2.val)
        l2 = l2.next
    l2_str += str(l2.val)
        
    l1_num, l2_num = int(l1_str[::-1]), int(l2_str[::-1])
    sum = l1_num + l2_num
    
    sum_str_rev = str(sum)[::-1]
    
    root = ListNode(0)
    curr = root
    for c in sum_str_rev:
        l_curr = ListNode(int(c))
        curr.next = l_curr
        curr = curr.next
        
    return root.next
