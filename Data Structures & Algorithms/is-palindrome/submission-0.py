class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while (l < r):
            while l < r and not self.alphaNum(s[l]): #keep moving pointer until alphanumeric value
                l+= 1
            while r > l and not self.alphaNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower(): #makes every char lowercase
                return False
            l+=1
            r-=1

        return True

    def alphaNum(self, c): #c is an alpha numeric value
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))