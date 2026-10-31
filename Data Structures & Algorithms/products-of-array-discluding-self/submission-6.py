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

        total_product = 1
        for num in nums:
            total_product *= num
        
        output = []
        for i, num in enumerate(nums):
            if num != 0:
                output.append(total_product // num)
            else:
                left = nums[:i]
                right = nums[i+1:]
                combined = left + right # list concatenation
                product = 1
                for survival in combined:
                    product *= survival
                output.append(product)
        return output



