class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # maximum = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         current = min(heights[i], heights[j]) * (j-i)
        #         # if current > maximum:
        #         #     maximum = current
        #         maximum = max(maximum, current) # a quicker way to get the maxmimum of two
        
        # return maximum

        # two pointer solution
        maximum = 0

        l, r = 0, len(heights)-1
        while l < r:
            current = min(heights[l], heights[r]) * (r-l)
            maximum = max(current, maximum)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
        return maximum
                
