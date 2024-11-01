class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        s = "(1+(4+5+2) -3)+(6+8)"
        s = -1+(2-(3+(4+5)))
        """
        
        
        stack = []
        sum = 0
        
        def cal2(i):
            if stack and (stack[-1] == '+' or stack[-1] == '-'):
                cal = stack.pop()
                if not stack or stack[-1] == '(':
                    if cal == '+':
                        sum_tmp =  i
                    else:
                        sum_tmp = 0 - i
                    stack.append(sum_tmp)
                    return
                sum_tmp = stack.pop()
                if cal == '+':
                    sum_tmp += i
                else:
                    sum_tmp -= i
                stack.append(sum_tmp)
            else:
                stack.append(i)
        idx = 0
        while idx < len(s):
            i = s[idx]
            if i == '(':
                stack.append(i)
            elif i == '+' or i == '-':
                stack.append(i)
            elif i >= '0' and i <= '9':
                current = 0
                while idx < len(s) and s[idx] >= '0' and s[idx] <= '9':
                    current = current*10 + int(s[idx])
                    idx += 1
                cal2(current)
                continue
            elif i == ')':
                sum_tmp = stack.pop()
                p = stack.pop()
                cal2(sum_tmp)
            elif i == ' ':
                idx += 1
                continue
            idx += 1
        return stack.pop()
    
    def calculate2(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign
    def calculate3(self, s):
        sign, current, res, stack = 1, 0, 0, []
        
        for c in s:
            if c.isdigit():
                current = current * 10 + int(c)
            elif c in '+-':
                res += sign * current
                if c == '+':
                    sign = 1
                else: 
                    sign = -1
                current = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                current = 0
                sign = 1
            elif c == ')':
                res += sign * current
                res *= stack.pop()
                res += stack.pop()
                current = 0
        return res + current * sign
s = Solution()
res = s.calculate3("1 + 1")
print(res)