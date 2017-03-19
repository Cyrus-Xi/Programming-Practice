#!/usr/bin/env python

def merge_ranges(list_ranges):
    if not list_ranges: raise Exception("Need to provide a non-empty list.")
    if any(x < 0 or y < 0 for (x, y) in list_ranges):
        raise Exception("Negative start/end times don't make sense.")
    if any(y < x for (x, y) in list_ranges):
        raise Exception("End times have to be greater than start times.")
    
    list_ranges.sort(key=lambda x: x[0])
    
    copy_ranges = list_ranges
    prev = list_ranges[0]
    
    # Another method of doing this would be to build up the copy element by element.
    # So could just modify the last element of the merged list.
    for i, (start, end) in enumerate(list_ranges[1:]):
        if start <= prev[1]:
            new_meet = (prev[0], max(prev[1], end))
            copy_ranges[i+1] = new_meet
            copy_ranges[i] = ('del', 'del')
            prev = new_meet
        else:
            prev = (start, end)
        
    return [(x, y) for (x, y) in copy_ranges if x != 'del']
        
          
print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
print merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9), (20, 23)])
print merge_ranges([(1,5), (2,3)])
