class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        # for char in s:
        #     dict_s[char] = dict_s.get(char, 0) + 1
        # for char in t:
        #     dict_t[char] = dict_t.get(char, 0) + 1
        for i in range(len(s)): # now s and t have the same length
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
        for key in dict_s:
            # if key not in dict_t:
            #     return False
            # if dict_s[key] != dict_t[key]:
            #     return False
            if dict_s[key] != dict_t.get(key, 0): # safer when a key does not exist
                return False
        return True