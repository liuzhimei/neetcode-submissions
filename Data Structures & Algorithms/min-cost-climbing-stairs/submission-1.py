class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Mathematically:
        # Denote f(i) by the min cost to reach index i.
        # f(i) = min(cost[i-1] + f(i-1), cost[i-2] + f(i-2))

        # # --- Method 1: naive recursion, too complex ---
        # def minCost(i): # the min cost to reach index i
        #     if i == 0:
        #         return 0
        #     if i == 1:
        #         return 0
        #     return min(cost[i-1] + minCost(i-1), cost[i-2] + minCost(i-2))
        # return minCost(len(cost))

        # --- Method 2: Top-down DP-memorization ---
        # store the function value f(i) in hashmap
        memo = {0: 0, 1: 0}
        def f(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(cost[i-1]+f(i-1), cost[i-2]+f(i-2)) 
                return memo[i]
        return f(len(cost)) # i=len(cost) is not index in the list, but the index next to the last index