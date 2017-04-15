def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_curr = 0
    max_so_far = 0
    for i, price in enumerate(prices[1:]):
        # not i-1 because iterating over prices[1:] already; ie prices[i+1] = prices[1:][i]
        max_curr = max(0, max_curr + price - prices[i])
        max_so_far = max(max_so_far, max_curr)
    return max_so_far
