class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Maxheap
        1) take distance of each point
        going through points find (distance, point)
        put into max heap of size k so space comlpexity is saved
        when more pop the highest value which will be too far away
        pop all at end and return
        """
        maxHeap = []
        result = []
        def calculateDistance(x,y):
            return ((x) ** 2 + (y) ** 2) ** 0.5
        for point in points:
            x,y = point
            distance = -1 * calculateDistance(x,y)
            heapq.heappush(maxHeap, (distance,point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        for value in maxHeap:
            distance, point = value
            result.append(point)
        return result
