# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # traverse according to adjacency list
        created = dict()
        visited = set()
        queue = []
        if not node:
            return node
        # create all nodes
        root = Node(node.val) # set neighbors to none firstly
        created[node.val] = root
        queue.append(node)
        while queue:
            curr = queue.pop()
            visited.add(curr)
            cloneCurr = created[curr.val]
            neighbors = []
            # append its neighbors
            for neighbor in curr.neighbors:
                if neighbor.val not in created:
                    tmp = Node(neighbor.val)
                    created[neighbor.val] = tmp
                else:
                    tmp = created[neighbor.val]
                if neighbor not in visited:
                    queue.append(neighbor)
                neighbors.append(tmp)
            cloneCurr.neighbors = neighbors
        return root
        
one = Node(1)
two = Node(2)
one.neighbors = [two]
two.neighbors = [one]

sol = Solution()
res = sol.cloneGraph(one)
print(res)      
        