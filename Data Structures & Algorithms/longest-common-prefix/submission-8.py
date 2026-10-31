class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # output = ""
        # dict_all = []
        # for i, string in enumerate(strs):
        #     dict_i = {} # key: index, value: char, for each string in the list strs
        #     for j, char in enumerate(string):
        #         dict_i[j] = char
            
        #     dict_all.append(dict_i)
        
        output = ""
        for i, char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    return output
                if char != strs[j][i]:
                    return output
            output = "".join([output, char])
        return output


