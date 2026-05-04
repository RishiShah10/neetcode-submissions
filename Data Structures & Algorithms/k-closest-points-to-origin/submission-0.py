import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        keep a min heap storing tuple (first is what the heap sorts on)
        tuple is (distance, (coords))
        keep heap of size k
        """
        result = []
        def calculateDistance(x1,y1):
            return math.sqrt((x1) ** 2 + (y1) ** 2)
        minHeap = []
        for point in points:
            x1,y1 = point
            distance = calculateDistance(x1,y1)
            heapq.heappush(minHeap, (distance,point))
        for i in range(k):
            dis,val = heapq.heappop(minHeap)
            result.append(val)
        return result

        