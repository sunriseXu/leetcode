class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def searchTarget(arr, target, start, end):
            if start == end:
                if arr[start] == target:
                    return start
                else:
                    return -1
            mid = (start + end) // 2
            if arr[mid] < target:
                return searchTarget(arr, target, mid + 1, end)
            else:
                return searchTarget(arr, target, start, mid)
        rowNum = -2
        for i in range(len(matrix)):
            if target < matrix[i][0]:
                rowNum = i - 1
                break
        if rowNum == -1:
            return False
        if rowNum == -2:
            rowNum = len(matrix) - 1
        res = searchTarget(matrix[rowNum], target, 0, len(matrix[rowNum]) - 1)
        if res == -1:
            return False
        return True

s = Solution()
res = s.searchMatrix(matrix = [[1],[3]], target = 3)
print(res)