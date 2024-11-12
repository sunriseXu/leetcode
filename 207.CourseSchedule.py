class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        [[1,0],[0,1]]
        numCourses = 2, prerequisites = [[1,0],[0,1]]
        """
        # what is this 
        preMap = {i : [] for i in range(numCourses)}
        for node, pre in prerequisites:
            preMap[pre].append(node)
        
        visited = set()
        def dfs(start):
            if not preMap[start]:
                return True
            if start in visited:
                return False

            visited.add(start)
            for pre in preMap[start]:
                if not dfs(pre):
                    return False
            visited.remove(start)
            preMap[start] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

s = Solution()
res = s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])
print(res)
        
        
        