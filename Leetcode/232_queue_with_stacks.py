#!/usr/bin/env python

class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """Push element x to the back of queue."""
        self.in_stack.append(x)

    def pop(self):
        """Remove the element from in front of queue and return that element."""
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        """Get the front element."""
        if not self.out_stack:
            # Flip ordering.
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]
        return self.out_stack[-1]

    def empty(self):
        """Return whether the queue is empty."""
        return len(self.in_stack) + len(self.out_stack) == 0
