class Solution:
    def rob(self, nums: List[int]) -> int:
        # if the last house nums[n-1] is included, then calculate the max money from nums[1] to nums[n-3], as a line problem rather than circular
        # if the last house is not included, then calculate the max money from nums[0] to nums[n-2], as a line problem rather than circular
        # So we need to construct the solution for the previous House Robber problem first as a helper function

        def lineRob(arr):
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]
            if len(arr) == 2:
                return max(arr[0], arr[1])
            prev = arr[0]
            curr = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                prev, curr = curr, max(arr[i] + prev, curr)
            return curr
        
        n = len(nums)
        return max(nums[n-1]+lineRob(nums[1:n-2]), lineRob(nums[:n-1]))