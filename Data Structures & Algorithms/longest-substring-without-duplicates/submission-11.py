class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # use sliding window and two pointers
        # if len(s) == 0:
        #     return 0
        
        # l, r = 0, 1
        # c_list = [s[0]]
        # longest = 1
        # while r < len(s):
        #     if s[r] not in c_list:
        #         c_list.append(s[r])
        #         r += 1
        #         longest = max(longest, len(c_list))
        #     else:
        #         idx = c_list.index(s[r])
        #         c_list = c_list[idx+1:]
        #         c_list.append(s[r])
        #         r += 1
        # return longest

        # ---- a better way -----
        hashset = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] not in hashset:
                hashset.add(s[r])
                longest = max(longest, r-l+1)
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                hashset.add(s[r])
        return longest

