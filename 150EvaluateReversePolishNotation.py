class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == '+':
                a = int(stack.pop(len(stack)-1))
                b = int(stack.pop(len(stack)-1))
                stack.append(a+b)
            elif i == '-':
                a = int(stack.pop(len(stack)-1))
                b = int(stack.pop(len(stack)-1))
                stack.append(b - a)
            elif i == '*':
                a = int(stack.pop(len(stack)-1))
                b = int(stack.pop(len(stack)-1))
                stack.append(a*b)
            elif i == '/':
                a = int(stack.pop(len(stack)-1))
                b = int(stack.pop(len(stack)-1))
                stack.append(int(b/a))
            else:
                stack.append(i)
        return stack[0]

sol = Solution()
res = sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
)
print(res)