def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_tups = []
    for i, num in enumerate(nums):
        diffs = [n[1] for n in nums_tups]
        if num in diffs:
            # diffs and nums are in sync
            return [diffs.index(num), i]
        else:
            nums_tups.append((num, target - num))
