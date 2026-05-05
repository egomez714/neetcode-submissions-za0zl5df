class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []      

        # stack : 2 1 + 3 3   
        for token in tokens:
            if token == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a,b = stack.pop(),stack.pop()
                stack.append(int( b / a))
            else:
                stack.append(int(token))
        return stack[0]