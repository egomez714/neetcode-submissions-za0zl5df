class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = [0]*26 

        for i in range(len(s)):
            ans[ord(s[i]) - ord('a')] += 1
            ans[ord(t[i]) - ord('a')] -= 1
        
        for count in ans:
            if count != 0:
                return False
        return True