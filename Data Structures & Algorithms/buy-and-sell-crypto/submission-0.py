class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_list, max_list = [], []
        min_val, max_val = prices[0], prices[len(prices)-1]
        for i in range(len(prices)):
            min_val = min(min_val, prices[i])
            min_list.append(min_val)
        for i in range(len(prices)-1, -1, -1):
            max_val = max(max_val, prices[i])
            max_list.append(max_val)
        max_list.reverse()
        profit = []
        for i in range(len(prices)):
            profit.append(max_list[i] - min_list[i])
        return max(profit)
