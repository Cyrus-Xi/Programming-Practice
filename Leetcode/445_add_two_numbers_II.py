# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1, c2 = l1, l2
        h1, h2 = c1, c2
        p1, p2 = None, None
        ct1 = ct2 = 0
        
        # Reverse lists so can start with least significant digit.
        while c1:
            ct1 += 1
            nxt = c1.next
            c1.next = p1
            if not nxt: break
            p1, c1 = c1, nxt
        while c2:
            ct2 += 1
            nxt = c2.next
            c2.next = p2
            if not nxt: break
            p2, c2 = c2, nxt

        # Left fill shorter list with 0s.
        shorter = h1 if ct1 < ct2 else h2 if ct2 < ct1 else 0
        if shorter:
            for i in xrange(abs(ct1 - ct2)):
                shorter.next = ListNode(0)
                shorter = shorter.next
        
        # Get sum linked list.
        carry = 0
        a = c3 = ListNode(0)
        while c1 and c2:
            v = c1.val + c2.val
            if carry: 
                v += carry
                carry = 0
            if v > 9:
                v -= 10
                carry = 1
            c3.next = ListNode(v)
            c1, c2, c3 = c1.next, c2.next, c3.next
        
        # Add carry node.
        if carry: c3.next = ListNode(1)
        
        # Reverse sum linked list so most significant digit is first.
        p3, ans = None, a.next
        while ans:
            nxt = ans.next
            ans.next = p3
            if not nxt: break
            p3, ans = ans, nxt

        return ans
