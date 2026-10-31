class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = set(numbers)
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference not in hashset:
                continue
            else:
                j = numbers.index(difference)
                if i == j:
                    continue
                return [i+1,j+1] if i < j else [j+1, i+1]
                    