class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # sort the integers in ascending order
        res = []
        combo = []

        def dfs(available, target):
            if sum(combo) == target:
                res.append(combo.copy())
                return
            if sum(combo) > target:
                return

            for i in range(len(available)):
                combo.append(available[i])
                dfs(available[i:], target)
                combo.pop()

        dfs(nums, target)
        return res
