#!/usr/bin/env python

def get_max_profit(prices):
    if len(prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')
    
    max_profit = prices[1] - prices[0]
    min_price = prices[0]
    
    # At i=0, would buy and sell at the same time.
    for price in prices[1:]:
        curr_profit = price - min_price
        max_profit = max(max_profit, curr_profit)
        min_price = min(min_price, price)
        
    return max_profit

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)
neg_prices = [5, 4, 3]
print get_max_profit(neg_prices)
