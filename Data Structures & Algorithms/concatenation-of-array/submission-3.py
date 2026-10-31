class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        idx = 0
        while idx < 2 * n:
            if idx < n:
                ans.append(nums[idx])
            else:
                ans.append(nums[idx-n])
            idx = idx + 1
        return ans

