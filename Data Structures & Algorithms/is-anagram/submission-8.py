class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mS = defaultdict(int)
        mT = defaultdict(int)
        for ch in s:
            mS[ch] += 1
        for ch in t:
            mT[ch] += 1
        return mS==mT
