class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = 0
        myMap = {}
        count = 0;
        longest = 0
        for r in range(len(s)):
            myMap[s[r]] = myMap.get(s[r],0) + 1
            freq = max(freq,myMap[s[r]])
            while r-l+1 - freq > k:
                myMap[s[l]] -= 1
                l+=1
            longest = max(longest,r-l+1)
        return longest