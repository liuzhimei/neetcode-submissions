class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # --- Method 1: backtracking (see 39.Combination Sum), but too inefficient ---
        # coins.sort()
        # res = []
        # path = []

        # def dfs(available, target):
        #     if sum(path) == target:
        #         res.append(path.copy())
        #         return
        #     if sum(path) > target:
        #         return
        #     for i in range(len(available)):
        #         path.append(available[i])
        #         dfs(available[i:], target)
        #         path.pop()
        
        # dfs(coins, amount)
        # if not res:
        #     return -1
        # num_coins = [len(x) for x in res]
        # return min(num_coins)


        # --- Method 2: DP ---
        # Denote f(k) as the min number of coins that sum up to k, with coins from coins. 
        # Then f(k) = min(f(k-coins[0])+1, ..., f(k-coins[len(coins)-1])+1) where k-coins[i]>0
        # Base case: f(coins[i]) = 1 for i = 0, ..., len(coins)-1, f(0) = 0

        # def f(k):
        #     if k == 0:
        #         return 0
        #     if k in coins:
        #         return 1
        #     if k < min(coins):
        #         return -1
        #     diff = []
        #     for i in range(len(coins)):
        #         if k - coins[i] > 0 and f(k-coins[i]) != -1:
        #             diff.append(f(k - coins[i]))
        #     if not diff:
        #         return -1
        #     return min(diff) + 1
        # return f(amount)


        memo = {0: 0}
        for k in coins:
            memo[k] = 1
        def f(k):
            if k in memo:
                return memo[k]
            else:
                if k < min(coins):
                    memo[k] = -1
                    return -1
                diff = []
                for i in range(len(coins)):
                    if k - coins[i] > 0 and f(k-coins[i]) != -1:
                        diff.append(f(k - coins[i]))
                if not diff:
                    memo[k] = -1
                    return -1
                memo[k] = min(diff) + 1
                return memo[k]
        return f(amount)
        





            