class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "emptylist"
        string = "+-".join(strs)
        return string

    def decode(self, s: str) -> List[str]:
        if s == "emptylist":
            return []
        return s.split("+-")