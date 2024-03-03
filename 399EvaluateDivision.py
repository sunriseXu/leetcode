class GraphNode:
    def __init__(self, label, neighbors):
        self.label = label
        self.neighbors = neighbors

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        hashmap = dict()
        for i in range(len(equations)):
            start = equations[i][0]
            end = equations[i][1]
            value = values[i]
            if start not in hashmap:
                startNode = GraphNode(start, [])
                hashmap[start] = startNode
            else:
                startNode = hashmap[start]
            
            if end not in hashmap:
                endNode = GraphNode(end, [])
                hashmap[end] = endNode
            else:
                endNode = hashmap[end]
            
            startNode.neighbors.append((value, endNode))
            endNode.neighbors.append(((1/value), startNode))
        
        res = []
        for q in queries:
            start = q[0]
            end = q[1]
            # traverse graph
            
            if start not in hashmap or end not in hashmap:
                res.append(-1)
                continue
            if start==end:
                res.append(1)
                continue
            queue = []
            visited = set()
            queue.append((1, hashmap[start]))
            visited.add(hashmap[start].label)
            find = False
            while queue:
                curr = queue.pop(0)
                currVal = curr[0]
                currNode = curr[1]
                
                for neighbor in currNode.neighbors:
                    neighborVal = neighbor[0]
                    neighborNode = neighbor[1]
                    neighborLabel = neighborNode.label
                    if neighborLabel in visited:
                        continue
                    nextVal = currVal * neighborVal
                    if neighborLabel == end:
                        res.append(nextVal)
                        find = True
                        break
                    visited.add(neighborLabel)
                    queue.append((nextVal, neighborNode))
                if find:
                    break
            if not find:
                res.append(-1)
        return res
sol = Solution()
res = sol.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
print(res)