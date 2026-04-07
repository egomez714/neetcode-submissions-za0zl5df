class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        longest = 0
        myDict = {}
        for r in range(len(s)):
            while s[r] in myDict:
                del myDict[s[l]]
                l+=1
            myDict[s[r]] = s[r]
            longest = max(r-l + 1,longest)
        return longest