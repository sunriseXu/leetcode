class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        smallestHeap = []
        output = []
        visited = []
        heapq.heapify(smallestHeap)
        heapq.heappush(smallestHeap, (nums1[0] + nums2[0], 0, 0))
        visited.append((0, 0))
        while k and smallestHeap:
            _, i, j = heapq.heappop(smallestHeap)
            output.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(smallestHeap, (nums1[i+1] + nums2[j], i+1, j))
                visited.append((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(smallestHeap, (nums1[i] + nums2[j+1], i, j+1))
                visited.append((i, j+1))
            k -= 1
        return output
s = Solution()
res = s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
print(res)

            