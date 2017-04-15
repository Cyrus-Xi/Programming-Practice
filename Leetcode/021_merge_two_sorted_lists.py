def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 or not l2: return l1 or l2
    
    c1, c2 = l1, l2
    l3 = p = ListNode(0)
        
    while c1 and c2:
        if c1.val <= c2.val:
            p.next = c1
            c1 = c1.next
        else:
            p.next = c2
            c2 = c2.next
        p = p.next
        
    p.next = c1 or c2
    
    return l3.next
