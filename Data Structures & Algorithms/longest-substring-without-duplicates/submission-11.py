class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        charTracker = set()
        longestSub = 0

        for right in range(len(s)):
            while s[right] in charTracker:
                charTracker.remove(s[left])
                left += 1
            charTracker.add(s[right])
            longestSub = max(longestSub, right - left + 1)
        return longestSub