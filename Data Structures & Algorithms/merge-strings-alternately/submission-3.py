class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # result = ""
        # for i in range(max(len(word1), len(word2))):
        #     if i < len(word1):
        #         result += word1[i]
        #     if i < len(word2):
        #         result += word2[i]
        # return result

        # Method 2: two pointer (equally efficient)
        result = []

        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[i:])

        return "".join(result)