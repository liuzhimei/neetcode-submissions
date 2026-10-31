class Solution:
    def isValid(self, s: str) -> bool:
        # while len(s) > 0:
        #     string_popped = False
        #     for i in range(len(s)-1):
        #         if s[i] == "(" and s[i+1] == ")":
        #             s = s[:i] + s[i+2:]
        #             string_popped = True
        #             break
        #         elif s[i] == "[" and s[i+1] == "]":
        #             s = s[:i] + s[i+2:]
        #             string_popped = True
        #             break
        #         elif s[i] == "{" and s[i+1] == "}":
        #             s = s[:i] + s[i+2:]
        #             string_popped = True
        #             break
        #         else:
        #             continue
        #     if string_popped is False:
        #         return False
        # return True

        # -------- use stack data structure ---------
        stack = []
        hashmap = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in hashmap:
                if not stack:
                    return False
                elif hashmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False

