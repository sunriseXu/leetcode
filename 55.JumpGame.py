class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        给一个序列，每个元素代表从该元素能够跳的最长距离，从第一个元素开始，判断是否能跳到最后一个元素
        从最后的元素开始往前数，能到达该元素的最远元素A选择为下一个节点。为什么一定要选择最远的元素。
        假设选择的并非最远的元素B，那么，元素A必然能够到达元素B，然后是元素C在A之前跳过A直接到达B。
        那么从元素C必然也能够达到元素A。
        """
        current = len(nums) - 1
        if current == 0:
            return 0
        count = 0
        while True:
            i = current 
            step = 0
            # flag = 0
            while i >= 0:
                i -= 1
                if i < 0:
                    break
                step += 1
                if nums[i] < step:
                    continue
                current = i
                # flag = 1 
            count += 1
            
            if current == 0:
                return count
    def canJump2(self, nums):
        """
        这里采用最近原则，因为考虑到全部元素都为1的情况，这种是最坏情况，时间复杂度为n方
        因此只选择第一个能够到达的元素进行遍历
        """
        current = len(nums) - 1
        if current == 0:
            return True
        while True:
            i = current 
            step = 0
            flag = 0
            while i >= 0:
                i -= 1
                if i < 0:
                    break
                step += 1
                if nums[i] < step:
                    continue
                current = i
                flag = 1 
                break
            if flag == 0:
                return False
            if current == 0:
                return True
        
 
s = Solution()
res = s.canJump2([0])
print(res)