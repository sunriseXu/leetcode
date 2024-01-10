# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        RecursionError: maximum recursion depth exceeded
        """
        cache = {}
        cacheHit = {'hit':0}
        def loop(height, start, end):
            if (start,end) in cache:
                cacheHit['hit'] = cacheHit['hit'] + 1
                return cache[(start, end)]
            
            if start >= end:
                cache[(start, end)] = 0
                return 0
            
            # double point
            tmpH = height[start]
            if tmpH > height[end]:
                tmpH = height[end]
            area = (end - start) * tmpH
            
            # case left
            tmpStart = start + 1
            tmpH = height[tmpStart]
            if tmpH > height[end]:
                tmpH = height[end]
            tmpA1 = (end - tmpStart) * tmpH
            if tmpA1 > area:
                res = loop(height, tmpStart, end)
                cache[(start, end)] = res
                return res
            # case right
            tmpEnd = end - 1
            tmpH = height[start]
            if tmpH > height[tmpEnd]:
                tmpH = height[tmpEnd]
            tmpA2 = (tmpEnd - start) * tmpH
            if tmpA2 > area:
                res = loop(height, start, tmpEnd)
                cache[(start, end)] = res
                return res
            
            tmp = loop(height, tmpStart, end)
            tmp2 = loop(height, start, tmpEnd)
            max = 0
            
            if tmp > tmp2:
                max = tmp
            else:
                max = tmp2
            if max < area:
                max = area
            cache[(start, end)] = max
            return max
        res = loop(height, 0, len(height)-1)
        return res
    def best(self, height):
        start = 0
        end = len(height) - 1
        area = 0
        while start < end:
            tmpH = height[start]
            if tmpH > height[end]:
                tmpH = height[end]
            tmpArea = (end - start) * tmpH
            area = max(tmpArea ,area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return area
            
sol = Solution()
res = sol.best([1,8,6,2,5,4,8,3,7])

print(res)


        