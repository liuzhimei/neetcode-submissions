class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # correct solution but not optimal
        # output = []
        # for i, num in enumerate(nums):
        #     left = nums[:i]
        #     right = nums[i+1:]
        #     combined = left + right # list concatenation
        #     product = 1
        #     for survival in combined:
        #         product *= survival
        #     output.append(product)
        # return output

        # # This is the solution if using division
        # total_product = 1
        # for num in nums:
        #     total_product *= num
        # output = []
        # for i, num in enumerate(nums):
        #     if num != 0:
        #         output.append(total_product // num)
        #     else:
        #         left = nums[:i]
        #         right = nums[i+1:]
        #         combined = left + right # list concatenation
        #         product = 1
        #         for survival in combined:
        #             product *= survival
        #         output.append(product)
        # return output

        # if we do not use division and aim for O(n) time
        # the key is to use array to store O(n) space
        output = [1] * len(nums) # initialize list with ones
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]
        return output





