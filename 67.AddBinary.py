class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        a = "1010", b = "1011"
        "10101"
        """
        length = max(len(a), len(b))
        res = []
        c = 0
        for i in range(length):
            abit , bbit = 0, 0
            if i < len(a):
                abit = int(a[~i])
            if i < len(b):
                bbit = int(b[~i])
            curr = (abit + bbit + c) % 2
            c = (abit + bbit +c) // 2
            res.insert(0, str(curr))
        if c == 0:
            return ''.join(res)
        res.insert(0, '1')
        return ''.join(res)

sol = Solution()
res = sol.addBinary("1010", "1011")
print(res)
            
            