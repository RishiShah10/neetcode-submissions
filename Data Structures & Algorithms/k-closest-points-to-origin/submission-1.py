import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        keep a max heap storing tuple (first is what the heap sorts on)
        tuple is (distance, (coords))
        keep heap of size k
        """
        def calculateDistance(x1,y1):
            return math.sqrt((x1) ** 2 + (y1) ** 2)
        maxHeap = []
        result = []
        for point in points:
            x1,y1 = point
            distance = -calculateDistance(x1,y1)
            heapq.heappush(maxHeap, (distance,point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        print(maxHeap)
        for index in maxHeap:
            dis,point = index
            result.append(point)
        return result

        