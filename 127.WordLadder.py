class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def addjWords(word, visited):
            res = []
            count = 0 
            for item in wordList:
                if item in visited:
                    continue
                for i in range(len(word)):
                    if word[i] != item[i]:
                        count += 1
                if count == 1:
                    res.append(item)
                count = 0
            return res
        # create addj map
        addjMap = {}
        visited = set()
        queue = []
        queue.append(beginWord)
        shortest = 0
        while queue:
            current = queue.pop(0)
            if current == endWord:
                return shortest - 1
            tmp = addjWords(current, visited)
            addjMap[current] = tmp
            visited.add(current)
            for i in tmp:
                queue.append(i)
                visited.add(i)
            shortest += 1
        return 0    
            
s = Solution()
res = s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"])
print(res)
