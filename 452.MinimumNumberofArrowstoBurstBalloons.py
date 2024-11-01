class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/solutions/1686627/c-java-python-6-lines-sort-and-greedy-image-explanation
        """
        # sort by end
        points.sort(key=lambda x: x[1])
        arrows = []
        for i in range(len(points)):
            if not arrows or arrows[-1] < points[i][0]:
                arrows.append(points[i][1])
        return len(arrows)
    
        
        
    
s = Solution()
res = s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
print(res)