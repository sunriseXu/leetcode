class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        # sorted
        current = 0
        largest = points[0][1]
        count = 0
        
        while current < len(points):
            current += 1
            if largest >= points[current][0]:
                if largest < points[current][1]:
                    largest = points[current][1]
            else:
                count += 1
        return count
            
s = Solution()
res = s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
print(res)