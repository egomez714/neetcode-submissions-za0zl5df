class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mS = defaultdict(int)
        mT = defaultdict(int)
        for i in range(len(s)):
            mS[s[i]] += 1
            mT[t[i]] += 1
        return mS==mT
