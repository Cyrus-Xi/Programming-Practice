#!/usr/bin/env python

# Challenge description:
# You are given two strings. Determine if the second string is a substring of the 
# first (Do NOT use any substr type library function). The second string may 
# contain an asterisk(*) which should be treated as a regular expression i.e. 
# matches zero or more characters. The asterisk can be escaped by a \ char in 
# which case it should be interpreted as a regular '*' character. To summarize: 
# the strings can contain alphabets, numbers, * and \ characters.

import sys
import fileinput

substring = True
escaped_ast = True

def is_substring(superstr, substr, super_index):
    global substring, escaped_ast
    curr = super_index
  
    sub_curr = 0
    escaped_ast = False
    length = len(superstr) - curr
        
    for sub_index, char in enumerate(substr):
        # Didn't find it.
        if curr >= len(superstr):
            substring = False
            break
        if char == "\\": 
            escaped_ast = True
            # Not followed by asterisk.
            if sub_index == len(substr)-1: 
                substring = False
                break
            if substr[sub_index+1] != "*":
                substring = False
                break
            # Skip.
            curr -= 1
        elif char == "*":
            if escaped_ast:
                if superstr[curr] != "*":
                    substring = False
                    escaped_ast = False
                    break
            else:
                # Asterisk last char.
                if sub_index == len(substr)-1: 
                    substring = True
                    break
                try:
                    index = curr + 1 + superstr[curr+1:].index(substr[sub_index+1])
                except ValueError:
                    substring = False
                    break
                except IndexError:
                    substring = False
                    break
                is_substring(superstr, substr[sub_index+1:], index)
                break
        else:
            if superstr[curr] != char:
                substring = False
                break
        curr += 1
        sub_curr += 1
        if sub_curr == len(substr)-1: substring = True

for line in fileinput.input():
    global substring, escaped_ast
    substring = True

    superstr = line.split(",")[0]
    substr = line[:-1].split(",")[1]

    curr_char = substr[0]
    if curr_char == "*":
        if len(substr) == 1: 
            print("true")
            continue
        else: 
            curr_char = substr[1]
            substr = substr[1:]
    elif curr_char == "\\": 
        if len(substr) <= 1: 
            print("false")
            continue
        else: 
            curr_char = substr[1]
            substr = substr[1]
            escaped_ast = True

    try:
        index = superstr.index(curr_char)
    except ValueError:
        print("false")
        continue

    is_substring(superstr, substr, index)

    # Do it for each instance of curr_char in super.
    for i in range(superstr.count(curr_char)-1):
        if substring: break
        try:
            index = superstr.index(curr_char, index+1)
            is_substring(superstr, substr, index)
        except ValueError:
            substring = False
            break

    if substring: print("true")
    else: print("false")
