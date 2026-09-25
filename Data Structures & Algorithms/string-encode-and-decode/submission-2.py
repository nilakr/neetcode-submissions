class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else: 
            result = " ".join(strs)
            return result

    def decode(self, s: str) -> List[str]:
        s = s.split(" ")
        return s