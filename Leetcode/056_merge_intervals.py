def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals: return intervals
    intervals.sort(key=lambda x: x.start)
    merged = [intervals[0]]
    for intvl in intervals[1:]:
        prev = merged[-1]
        if intvl.start <= prev.end:
            new_end = max(prev.end, intvl.end)
            merged[-1] = Interval(prev.start, new_end)
        else:
            merged.append(intvl)
    return merged
