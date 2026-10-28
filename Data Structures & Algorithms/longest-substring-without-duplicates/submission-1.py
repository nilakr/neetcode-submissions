class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        map = set()
        left = 0

        #i = 0

        for i in range(len(s)):
            while (s[i] in map):
                map.remove(s[left])
                left += 1

            map.add(s[i])
            maxLength = max(maxLength, i - left + 1)

        return maxLength

            

    



