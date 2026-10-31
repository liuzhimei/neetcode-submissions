class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # ----- time complexity: O(n), space complexity: O(n), not the best -----
        # min_list, max_list = [], []
        # min_val, max_val = prices[0], prices[len(prices)-1]
        # for i in range(len(prices)):
        #     min_val = min(min_val, prices[i])
        #     min_list.append(min_val)
        # for i in range(len(prices)-1, -1, -1):
        #     max_val = max(max_val, prices[i])
        #     max_list.append(max_val)
        # max_list.reverse()
        # profit = []
        # for i in range(len(prices)):
        #     profit.append(max_list[i] - min_list[i])
        # return max(profit)

        # ------ sliding window technique with space complexity O(1) -----
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            current_profit = prices[r] - prices[l]
            max_profit = max(max_profit, current_profit)
            if current_profit > 0:
                r += 1
            else:
                l = r
                r = l + 1
        return max_profit
