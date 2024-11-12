class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preMap = {i:[] for i in range(numCourses)}
        for node, pre in prerequisites:
            preMap[node].append(pre)
            
        result = []
        visited, cycle = set(), set()
        
        def dfs(start):
            if start in visited:
                return True
            if start in cycle: 
                return False
            cycle.add(start)
            for i in preMap[start]:
                tmpRes = dfs(i)
                if not tmpRes:
                    return False
                
            cycle.remove(start)
            visited.add(start)
            result.append(start)
            return True
        
        for i in range(numCourses):
            tmp = dfs(i)
            if not tmp:
                return []
            
        return result

s = Solution()
res = s.findOrder(numCourses = 4, prerequisites = [[2,0],[2,1],[0,3],[1,3]])
print(res)