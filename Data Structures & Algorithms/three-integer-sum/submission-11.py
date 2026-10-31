class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort() # important for using two-pointer
        for i in range(len(nums)):
            target = - nums[i]

            l, r = i+1, len(nums)-1 # ordered triplets to avoid duplicates
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    solution = [nums[i], nums[l], nums[r]] 
                    if solution not in output:
                        output.append(solution)

                    # after finding a solution, need to either increase l by 1, or decrease r by 1! otherwise the while loop get stuck at here and never exit the loop!
                    l += 1
            
        return output



