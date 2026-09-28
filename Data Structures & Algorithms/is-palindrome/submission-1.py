class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            while l < r and not s[l].isalnum(): #keep moving pointer until alphanumeric value
                l+= 1
            while r > l and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower(): #makes every char lowercase
                return False
            l+=1
            r-=1

        return True