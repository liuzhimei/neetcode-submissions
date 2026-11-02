class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # let f(i,j) be the number of unique ways to reach bottom-right from a i*j grid
        # Then f(i,j) = f(i, j-1) + f(i-1, j)

        # # --- Method 1: bruteforce recursion ---
        # def f(i, j):
        #     if i == 0 and j == 0:
        #         return 0
        #     if i == 1 and j == 0:
        #         return 1
        #     if i == 0 and j == 1:
        #         return 1
        #     return f(i, j-1) + f(i-1, j)
        # return f(m, n)

        # # --- Method 2: top-down DP-memorisation ---
        # memo = {(1,1): 1, (2,1): 1, (1,2): 1}
        # def f(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     else:
        #         if i == 1 or j == 1:
        #             memo[(i,j)] = 1
        #             return memo[(i,j)]
        #         memo[(i,j)] = f(i,j-1) + f(i-1,j)
        #         return memo[(i,j)]
        # return f(m,n)
        
        # --- Method 3: bottom-up DP-tabulation ---
        if m == 1 or n == 1:
            return 1
        dp = [[0] * n for _ in range(m)]
        dp[0] = [1] * n
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

        # How to use advanced method with time O(m*n) and space O(n)?

        
        