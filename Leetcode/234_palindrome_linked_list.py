#!/usr/bin/env python

def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    
    # get middle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    # handle odd case
    if fast:
        slow = slow.next
    
    # reverse 2nd half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
        
    # compare 
    while prev:
        if prev.val != head.val: return False
        prev, head = prev.next, head.next
        
    return True
