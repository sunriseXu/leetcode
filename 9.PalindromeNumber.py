class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        121 1
        1 1
        2 12
        1 121
        """
        ori = x
        flag = True
        if x < 0:
            return False
        reverse = 0
        while ori:
            tmp = ori % 10
            ori = ori // 10
            reverse = reverse * 10 + tmp

        
        if x == reverse:
            return True
        else:
            return False
        
sol = Solution()
res = sol.isPalindrome(-121)
print(res)

            
                    