#!/usr/bin/env python

import fileinput

def evaluate(expression):
    num_stack = []
    op_stack = []
    expr_split = expression.split()
    zero = False
    
    for token in expr_split:
        if token == "+" or token == "*" or token == "/":
            op_stack.append(token)
        else:
            num_stack.append(int(token))
    result = 0
    
    # Actually want queue-like behavior for nums.
    num_stack.reverse()
    
    while op_stack:
        op = op_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        
        # With division, num2 / num1.
        if op == "+":
            result = num1 + num2
        elif op == "*":
            result = num1 * num2
        else:
            try:
    	        result = num1 / num2
            except ZeroDivisionError:
                print(0)
                zero = True
                break
            
        num_stack.append(result)
        
    if not zero:
    	print(int(round(num_stack.pop())))
    
for index, line in enumerate(fileinput.input()):
	evaluate(line)

