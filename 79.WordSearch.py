class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        seen = list()
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rowLen = len(board)
        colLen = len(board[0])
        
        def traverse(i, j, wlen):
            if wlen == len(word):
                return True
            
            for di in direction:
                newi = i + di[0]
                newj = j + di[1]
                if 0 <= newi < rowLen and 0 <= newj < colLen and (newi, newj) not in seen and board[newi][newj] == word[wlen]:
                    seen.append((newi, newj))
                    res = traverse(newi, newj, wlen + 1)
                    seen.pop()
                    if res:
                        return True
            return False
        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == word[0]:
                    seen.append((i, j))
                    res = traverse(i, j, 1)
                    seen.pop()
                    if res:
                        return True
        return False

s = Solution()
res = s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
print(res)
                
                    