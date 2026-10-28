class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        map = set()
        left = 0

        for i in range(len(s)):
            while (s[i] in map): #when the letter is already found in the set
                map.remove(s[left]) #remove left most in sliding window
                left += 1 #keep removing until it no longer has repeated vals

            map.add(s[i])
            maxLength = max(maxLength, i - left + 1)

        return maxLength

            

    



