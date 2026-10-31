class Solution:
    def trap(self, height: List[int]) -> int:
        ## Too complex: O(n^2) time complexity, O(n) space complexity
        # water = {} # key: idx, value: max water current idx holds
        # l, r = 0, len(height)-1
        # while l <= r:
        #     for i in range(l+1, r):
        #         vol = min(height[l], height[r]) - height[i] # can be negative
        #         water[i] = max(vol, water.get(i, 0))
        #     if height[l] > height[r]:
        #         r -= 1
        #     else:
        #         l += 1
        # result = 0
        # for key in water:
        #     result += water[key]

        # return result

        # O(n) time complexity, O(n) space complexity solution:
        left_max_list, right_max_list = [], []
        left_max, right_max = 0, 0
        for i in range(len(height)):
            left_max = max(left_max, height[i])
            left_max_list.append(left_max)
        for i in range(len(height)-1, -1, -1):
            right_max = max(right_max, height[i])
            right_max_list.append(right_max)
        right_max_list.reverse()

        result = 0
        for i in range(len(height)):
            vol = min(left_max_list[i], right_max_list[i]) - height[i]
            if vol > 0:
                result += vol
        
        return result

        