class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} # key: elements of nums; val: frequency

        for i, number in enumerate(nums):
            d[number] = d.get(number, 0) + 1
        
        freq_list = []
        for key, val in d.items():
            freq_list.append([key, val])
        
        freq_list.sort(key=lambda x: -x[1])

        output = []
        for j in range(k):
            output.append(freq_list[j][0])
        return output

