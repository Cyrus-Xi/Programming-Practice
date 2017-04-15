def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prev = -1
    for n in sorted(nums):
        if n != prev + 1: return prev + 1
        prev = n
    
    return prev + 1
