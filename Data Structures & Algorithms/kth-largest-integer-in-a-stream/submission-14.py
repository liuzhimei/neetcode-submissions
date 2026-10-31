class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        # heapify the starting list and pop out the n-k smallest values
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)


    def add(self, val: int) -> int:
        # # construct max heap
        # nums_neg = []
        # for i in range(len(self.nums)):
        #     nums_neg.append(- self.nums[i])
        # heapq.heapify(nums_neg)
        # heapq.heappush(nums_neg, - val)
        # for i in range(self.k - 1):
        #     heapq.heappop(nums_neg)
        # self.nums.append(val)
        # return - nums_neg[0]

        # ---- Method 2 ----
        # Use min heap instead, because we can always pop the values smaller than the kth largest value
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]

