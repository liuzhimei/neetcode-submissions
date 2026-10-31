class Solution:
    def climbStairs(self, n: int) -> int:
        # Mathematically: 
        # denote f(n) as the number of distinct ways to climb to the n-th staircase.
        # The last move to reach n-th staircase can be a 2-step move, or a 1-step move, corresponding to f(n-2) and f(n-1) ways to reach the (n-2)-th and (n-1)-th staircase, respectively
        # Difference equation is: f(n) = f(n-1) + f(n-2)
        # Base case: f(1) = 1, f(2) = 2

        # # -- Method 1: naive recursive --
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # -- Method 2: top-down DP-memorization (still a recursive method) --
        memo = {1: 1, 2: 2} # key: n, val: f(n)

        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = f(n-1) + f(n-2)
                return memo[n]
        return f(n)
