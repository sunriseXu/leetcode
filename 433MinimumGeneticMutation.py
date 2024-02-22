class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        queue = []
        visited = set()
        dist = {}
        for i in bank:
            dist[i] = float('inf')
        def findOneMuation(curr, visited):
            res = []
            for muation in bank:
                count = 0
                for i in range(len(muation)):
                    if curr[i] != muation[i]:
                        count += 1
                if count == 1 and muation not in visited:
                    res.append(muation)
            return res
        
        init = findOneMuation(startGene, visited)
        for i in init:
            visited.add(i)
            queue.append(i)
            dist[i] = 1
        
        while queue:
            curr = queue.pop(0)
            if curr == endGene:
                return dist[curr]
            next = findOneMuation(curr, visited)
            for i in next:
                visited.add(i)
                queue.append(i)
                dist[i] = min(dist[i], dist[curr] + 1)
        return -1
            
sol = Solution()
res = sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"])
print(res)  
