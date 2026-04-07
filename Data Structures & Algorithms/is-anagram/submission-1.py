class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False

        solS, solT = {}, {}

        for i in range(len(s)):
            solS[s[i]] = 1 + solS.get(s[i],0)
            solT[t[i]] = 1 + solT.get(t[i],0)
        return solS == solT