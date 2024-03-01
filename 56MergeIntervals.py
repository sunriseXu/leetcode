class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        class comparatorA:
            def __init__(self, interval):
                self.interval = interval
            def __lt__(self, other):
                return self.interval[0] < other.interval[0]
        newIntervals = [comparatorA(i) for i in intervals]
        newIntervals.sort()
        
        res = []
        curr = 0
        stayX = False
        stayY = False
        while curr + 1 < len(intervals):
            # 3 conditions
            if not stayX:
                startx = newIntervals[curr].interval[0]
            if not stayY:
                currY = newIntervals[curr].interval[1]
            nextX = newIntervals[curr + 1].interval[0]
            nextY = newIntervals[curr + 1].interval[1]
            if currY < nextX:
                # result found
                res.append([startx, currY])
                curr += 1
                stayX = False
                stayY = False
            elif currY < nextY:
                curr += 1
                stayX = True
                stayY = False
            else:
                curr += 1
                stayX = True
                stayY = True
        if not stayX:
            startx = newIntervals[curr].interval[0]
        if not stayY:
            currY = newIntervals[curr].interval[1]
        res.append([startx, currY])
        return res
    def merge2(self, intervals):
        intervals.sort(key = lambda x : x[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            elif res[-1][1] < intervals[i][1]:
                res[-1][1] = intervals[i][1]                
        return res
        
sol = Solution()
sol.merge2([[1,4],[2,3]])