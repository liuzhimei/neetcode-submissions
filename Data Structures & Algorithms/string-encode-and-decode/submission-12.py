class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     if strs == []:
    #         return "emptylist"
    #     string = "+-".join(strs)
    #     return string

    # def decode(self, s: str) -> List[str]:
    #     if s == "emptylist":
    #         return []
    #     return s.split("+-")

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i, s in enumerate(strs):
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        while len(s) > 0:
            s_list = s.split("#")
            first_char_len = int(s_list[0])
            output.append(s[len(s_list[0]) + 1 : len(s_list[0]) + 1 + first_char_len])
            s = s[len(s_list[0]) + 1 + first_char_len:]
        return output


