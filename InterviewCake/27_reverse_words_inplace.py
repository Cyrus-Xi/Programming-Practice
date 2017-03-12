#!/usr/bin/env python

import string

def reverse_chars(s_lst, l, r):
    while l < r:
        s_lst[l], s_lst[r] = s_lst[r], s_lst[l]
        l, r = l + 1, r - 1
    return s_lst

def reverse_words(sentence):
    sentence = list(sentence)
    space = set(string.whitespace)
    # Reverse all chars.
    reverse_chars(sentence, 0, len(sentence) - 1)
    l = 0
    # (Re-)reverse chars in words.
    # Go one further to ensure we reverse the last word too.
    for i in xrange(len(sentence) + 1):
        if i == len(sentence) or sentence[i] in space:
            reverse_chars(sentence, l, i - 1)
            l = i + 1
    return ''.join(sentence)
        
assert reverse_words('Jack climbed the beanstalk') == 'beanstalk the climbed Jack'
print 'Test passed!'
