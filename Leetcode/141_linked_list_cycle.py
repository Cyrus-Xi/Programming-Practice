def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    cur1, cur2 = head, head
    
    while cur1 and cur2:
        cur1 = cur1.next
        cur2 = cur2.next
        if cur2: cur2 = cur2.next
        else: break
        if cur1 == cur2: return True
    
    return False
