class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for point in points:
            x,y = point[0],point[1]
            dis = (x ** 2) + (y ** 2)
            heapq.heappush(heap,(-dis,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        for value in heap:
            neg_dis,x,y = value
            result.append([x,y])
        return result

        