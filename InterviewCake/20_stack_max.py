#!/usr/bin/env python

class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    # at each position in the stack, keep track of the max element
    # from there down
    def push(self, item):
        if not self.items: tup = (item, item)
        else: tup = (item, max(item, self.items[-1][1]))
        self.items.append(tup)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[-1]
    
    # max of the whole stack equals the max of the top element
    def get_max(self):
        if not self.items: return None
        return self.items[-1][1]
    

s = Stack()
s.push(3)
s.push(5)
print s.get_max()
s.push(4)
print s.get_max()
s.push(11)
s.push(2)
print s.get_max()
s.pop()
s.pop()
print s.get_max()
