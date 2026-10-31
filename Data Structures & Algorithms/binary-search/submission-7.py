class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # brute force method with time complexity O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        # # ----- binary search method with time complexity O(logn) -----
        # # use the idea of left pointer and right pointer from two pointer
        # l, r = 0, len(nums)-1
        # while l <= r:
        #     if l + 1 == r:
        #         if nums[l] == target:
        #             return l
        #         elif nums[r] == target:
        #             return r
        #         else:
        #             return -1
        #     if len(nums) == 1 and nums[0] != target:
        #         return -1
        #     mid_idx = int((r-l) / 2) + l
        #     if nums[mid_idx] == target:
        #         return mid_idx
        #     elif nums[mid_idx] > target:
        #         r = mid_idx
        #     else:
        #         l = mid_idx
        # return -1

        # ----- make above code more efficient ------
        l, r = 0, len(nums)-1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1


