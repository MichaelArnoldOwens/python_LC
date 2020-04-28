class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set = set()
        left = 0
        right = 0
        longest = 0
        curr = 0
        while left < len(s) and right < len(s):
            if s[right] in _set:
                _set.remove(s[left])
                curr -= 1
                left += 1
            else:
                _set.add(s[right])
                curr += 1
                right += 1
                longest = max(longest, curr)
        return longest