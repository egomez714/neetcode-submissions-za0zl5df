class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            myDictOne = {}
            myDictTwo = {}
            for i in range(len(s)):
                myDictOne[s[i]] = myDictOne.get(s[i],0) + 1
            for i in range(len(t)):
                myDictTwo[t[i]] = myDictTwo.get(t[i],0) + 1
            return myDictOne == myDictTwo