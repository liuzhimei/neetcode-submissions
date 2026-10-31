class Solution:
    def rob(self, nums: List[int]) -> int:
        # Mathematically:
        # Define f(i) as the max money robbed among the houses before and include index i, with the money from index i being robbed too.
        # Then the difference equation is:
        # f(i) = max(f(i-1), f(i-2)+nums[i], f(i-3)+nums[i])

        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        # if len(nums) == 3:
        #     return max(nums[1], nums[0]+nums[2])
        
        # # --- Method 1: top-down DP-memorisation, too complex ---
        # def f(i):
        #     memo = {0: nums[0], 1: nums[1], 2: nums[0]+nums[2]}
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(f(i-1), f(i-2) + nums[i], f(i-3) + nums[i])
        #     return memo[i]

        # return max(f(len(nums)-1), f(len(nums)-2))

        # # --- Method 2: bottom-up DP-tabulation, iteration ---
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = nums[1]
        # dp[2] = nums[0] + nums[2]
        # for i in range(3, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-3]+nums[i])
        # return max(dp[len(nums)-1], dp[len(nums)-2])

        # ----------------------------------------------

        # A better way to think as a Markov chain is to condition on the existence of the last house
        # Define f(i) to denote the max money from robbing nums[:i+1]. We don't care whether index i is robbed or not.
        # Let len(nums)=n. Then f(n-1) = max(nums[n-1]+f(n-3), f(n-2)), where nums[-1]+f(n-3) corresponds to the case when last house must be robbed, and f(n-3) is the max money from index n-3 and before; or we don't rob last house, then we consider the max money from index n-2 and before
        # Generally, f(i) = max(nums[i] + f(i-2), f(i-1))

        # # --- Method 1 ---
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        # memo = {0: nums[0], 1: max(nums[0], nums[1])}
        # def f(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(nums[i] + f(i-2), f(i-1))
        #         return memo[i]
        # return f(len(nums)-1)

        # --- Method 2 ---
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev = nums[0] # i=0
        curr = max(nums[0], nums[1]) # i=1
        for i in range(2, len(nums)):
            prev, curr = curr, max(nums[i] + prev, curr)
        return curr
