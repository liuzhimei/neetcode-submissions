class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list_strs = []
        
        # for j in range(len(strs)):
        #     d = {} # key: char, val: count
        #     for i, char in enumerate(strs[j]):
        #         d[char] = d.get(char, 0) + 1
            
        #     list_strs.append(d)

        hashmap = {}

        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str in hashmap:
                value = hashmap[sorted_str] # should be a list
                value.append(strs[i])
                hashmap[sorted_str] = value
            else:
                hashmap[sorted_str] = [strs[i]]


            # hashmap[sorted_str] = hashmap.get(sorted_str, []).append(strs[i])
        
        output = []
        for key, value in hashmap.items():
            output.append(value)
        
        return output




