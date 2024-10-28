class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        '''
        gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        if you start from a, and stuck at b, then you can't start from any station between a and b.
        也就是说排除法，走过的路如果不通，那么中间的任何一条路都不通
        '''
        # start from 0, find first stuck station
        start = 0
        fly = 0
        while True:
            # find next stuck point
            i = start 
            current = gas[i]
            flag = 0
            init = True
            while init or i != start:
                init = False
                current = current - cost[i]
                if current < 0:
                    # stuck , break
                    if start + 1 >= len(gas):
                        return -1
                    start = (i+1) % len(gas)
                    flag = 1
                    break
                i = (i+1) % len(gas)
                if i + 1 >= len(gas):
                    fly = 1
                current = current + gas[i]
                
            if flag == 0:
                # find answer
                return start
            if flag == 1 and fly == 1:
                return -1

s = Solution()
res = s.canCompleteCircuit(gas = [4,5,2,6,5,3], cost = [3,2,7,3,2,9])
print(res)