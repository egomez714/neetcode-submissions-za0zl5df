class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        m = { ')': '(',']':'[','}':'{'}

        for c in s:
            if c in m:
                if res and res[-1] == m[c]:
                    res.pop()
                else:
                    return False
            else:
                res.append(c)
        return True if len(res)==0 else False