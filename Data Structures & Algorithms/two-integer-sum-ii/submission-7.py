class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashset = set(numbers) # However, here space complexity is O(n). We need O(1)
        # for i in range(len(numbers)): # Time complexity: O(n)
        #     difference = target - numbers[i]
        #     if difference not in hashset:
        #         continue
        #     else:
        #         j = numbers.index(difference)
        #         if i == j:
        #             continue
        #         return [i+1,j+1] if i < j else [j+1, i+1] # make sure in the form [a,b] with a<b
                    
        # Use the idea of two pointer and use the information that the list is sorted in ascending order
        l, r = 0, len(numbers)-1

        while l < r: # always can satisfy as we are guaranteed to find a solution
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
