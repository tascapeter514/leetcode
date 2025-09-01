# 121. Best Time to Buy and Sell Stock
# Solved
# Easy
# Topics
# premium lock iconCompanies

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

test_one = {
    'input': {
        'prices': [7,1,5,3,6,4]
    },
    'output': 5
}


test_two = {
    'input': {
        'prices': [7,6,4,3,1]
    },
    'output': 0
}

class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                left = right          
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                print(max_profit)
            right += 1
        print(max_profit)
           

Sol = Solution()

Sol.maxProfit(test_one['input']['prices'])