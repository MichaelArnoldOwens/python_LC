
import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            length = max(len1, len2)
            if length > end -start:
                start = i - math.floor((length - 1) / 2)
                end = i + math.floor(length / 2)
        end += 1
        return s[start:end]
            
            
            
            
            
    def expand(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
