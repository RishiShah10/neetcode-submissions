class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for point in points:
            x,y = point[0],point[1]
            dis = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap,(dis,point))
        print(heap)
        for i in range(k):
            val = heapq.heappop(heap)
            dis,item = val
            res.append(item)
        return res

        