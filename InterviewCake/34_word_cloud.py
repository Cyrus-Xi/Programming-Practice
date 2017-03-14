#!/usr/bin/env python

import string

def build_word_cloud_dict(s, freqs=None):
    # Lowercase and remove extraneous whitespace and punctuation.
    if not freqs: freqs = {}
    for w in s.split():
        if w in string.whitespace: continue
        # Remove punctuation from ends of word.
        w = ''.join(c for i, c in enumerate(w.lower()) 
                    if 0 < i < len(w) - 1 or c not in string.punctuation)
        freqs[w] = freqs.get(w, 0) + 1
    return freqs
           
s1 = 'After making a real gung-ho effort to beat the eggs, Dana read the next step: '
s2 = 'Add milk and eggs, then add flour and sugar.'
d1 = build_word_cloud_dict(s1)
d2 = build_word_cloud_dict(s2, d1)
print d2

s3 = "We came, we saw, we conquered ... then we ate Bill's (Mille-Feuille) cake."
s4 = 'The bill came to five dollars.'
d3 = build_word_cloud_dict(s3)
d4 = build_word_cloud_dict(s4, d3)
print d4
