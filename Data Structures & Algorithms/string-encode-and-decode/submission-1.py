class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: #if the list is empty
            return 
        result = " ".join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        s = s.split(" ")
        return s