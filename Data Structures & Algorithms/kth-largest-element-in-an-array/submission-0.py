class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest = (n-k+1)th smallest
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]