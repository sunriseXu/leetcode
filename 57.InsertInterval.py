class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
        """
        res = []
        intervals.insert(0, [-float("inf"), -float("inf")])
        intervals.append([float("inf"), float("inf")])
        
        def createRes(startIdx, endIdx, kind):
            for i in range(startIdx):
                res.append(intervals[i])
            if kind == 0:
                res.append([intervals[startIdx][0], intervals[endIdx - 1][1]])
                
            elif kind == 1:
                res.append([intervals[startIdx][0], newInterval[1]])
            elif kind == 3:
                res.append([newInterval[0], intervals[endIdx - 1][1]])
            else:
                res.append([newInterval[0], newInterval[1]])
            for i in range(endIdx, len(intervals)):
                res.append(intervals[i])            
        
        start_index = -1
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                start_index = i
                break
        
        end_index = -1
        for i in range(len(intervals)):
            if intervals[i][1] > newInterval[1]:
                end_index = i
                break
        # 4 situation
        # start_index in and out
        # end_index in and out
        
        if intervals[start_index-1][1] >= newInterval[0]:
            # start in 
            if intervals[end_index][0] <= newInterval[1]:
                createRes(start_index - 1 , end_index + 1, 0)
            else:
                # end in
                createRes(start_index - 1, end_index, 1)
        else:
            if intervals[end_index][0] <= newInterval[1]:
                # end in
                createRes(start_index , end_index + 1, 3)
            else:
                # end in
                createRes(start_index , end_index, 4)
        return res[1:-1]

s = Solution()
res = s.insert(intervals = [], newInterval = [17,18])
print(res)