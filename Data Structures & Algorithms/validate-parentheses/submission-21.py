class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end = { '}': '{',']': '[',')': '(' }

        for c in s:
            if c not in end:
                stack.append(c)
            else:
                if stack and stack[-1] == end[c]:
                    stack.pop()
                else:
                    return False
            
        return True if len(stack) == 0 else False