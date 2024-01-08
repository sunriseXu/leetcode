# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        start = -2
        end = -2
        flowerbedLen = len(flowerbed)
        plantedIdx = []
        for i in range(0, flowerbedLen):
            if flowerbed[i] == 1:
                plantedIdx.append(i)
        plantedIdx.append(flowerbedLen+1)
        idx = 0
        canPlantAllNumber = 0
        for idx in range(0, len(plantedIdx)):
            start = end
            end = plantedIdx[idx]
            canPlantRangeStart = start + 2
            canPlantRangeEnd = end - 2
            canPlantRangeSize = canPlantRangeEnd - canPlantRangeStart + 1
            if canPlantRangeSize > 0:
                if canPlantRangeSize % 2 == 0:
                    currentSize = int(canPlantRangeSize / 2)
                else:
                    currentSize = int(canPlantRangeSize / 2) + 1
                canPlantAllNumber += currentSize
        if canPlantAllNumber >= n:
            return True
        else:
            return False
            
sol = Solution()
res = sol.canPlaceFlowers([1,0,0,0,1,0,0], 2)
print(res)