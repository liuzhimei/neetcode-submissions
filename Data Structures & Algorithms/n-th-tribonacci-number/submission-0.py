class Solution:
    def tribonacci(self, n: int) -> int:
        # # --- Method 1: native recursion ---
        # def T(i):
        #     if i == 0:
        #         return 0
        #     if i == 1:
        #         return 1
        #     if i == 2:
        #         return 1
        #     return T(i-1) + T(i-2) + T(i-3)
        # return T(n)

        # # --- Method 2: bottom-up DP-tabulation ---
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 1
        # dp = [0] * (n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # return dp[n]

        # --- Method 3: advanced ---
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        prev1 = 0
        prev2 = 1
        curr = 1
        for i in range(3, n+1):
            prev1, prev2, curr = prev2, curr, prev1 + prev2 + curr
        return curr