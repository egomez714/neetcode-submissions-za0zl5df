class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        m = { ')': '(',']':'[','}':'{'}

        for i in range(len(s)):
            if s[i] in m:
                if res and res[-1] == m[s[i]]:
                    res.pop()
                else:
                    return False
            else:
                res.append(s[i])
        return True if len(res) == 0 else False