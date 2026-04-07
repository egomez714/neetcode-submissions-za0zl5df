class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        myDict = {}
        maxFreq = 0
        for r in range(len(s)):
            myDict[s[r]] = myDict.get(s[r],0) + 1
            maxFreq = max(maxFreq,myDict[s[r]])
            while r-l+1 - maxFreq > k:
                myDict[s[l]] -= 1
                l+=1
        return r-l+1

            

            