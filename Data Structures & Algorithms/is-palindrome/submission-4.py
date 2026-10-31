class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean up the input string
        s_lower = s.lower() # convert all letters to lower case; note strings are immutable, so s stays the same
        s_compact = "".join(c for c in s_lower if c.isalnum()) # remove all white spaces inside a string

        for i in range(len(s_compact)):
            if s_compact[i] != s_compact[len(s_compact)-i-1]:
                return False
        
        return True