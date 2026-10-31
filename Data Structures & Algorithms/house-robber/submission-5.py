class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[1], nums[0]+nums[2])
        
        # # --- Method 1: top-down DP-memorisation, too complex ---
        # def f(i):
        #     memo = {0: nums[0], 1: nums[1], 2: nums[0]+nums[2]}
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(f(i-1), f(i-2) + nums[i], f(i-3) + nums[i])
        #     return memo[i]

        # return max(f(len(nums)-1), f(len(nums)-2))

        # --- Method 2: bottom-up DP-tabulation, iteration ---
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i], dp[i-3]+nums[i])
        return max(dp[len(nums)-1], dp[len(nums)-2])

        