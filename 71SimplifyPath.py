class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathArr = path.split('/')
        stack = []
        for i in pathArr:
            if i == '':
                continue
            if i == '..':
                if len(stack) > 0:
                    stack.pop(len(stack)-1)
            elif i == '.':
                continue
            else:
                stack.append(i)
        return '/'+'/'.join(stack)

sol = Solution()
res = sol.simplifyPath("/a/./b/../../c/")
print(res)