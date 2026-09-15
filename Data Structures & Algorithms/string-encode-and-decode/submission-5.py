class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s): #still has more left in string
            j = i
            while (s[j] != "#"): #going until the # delimiter 
                j += 1
            length = int(s[i:j]) #takes out just the length of the word
            result.append(s[j + 1 : j + length + 1])
            i = j + length + 1

        return result

        

