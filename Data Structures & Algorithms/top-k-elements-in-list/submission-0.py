class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = defaultdict(int)
        heap = []
        toReturn = []
        for num in nums:
            myMap[num] += 1
        for key,value in myMap.items():
            heapq.heappush(heap, (-value, key))
        for i in range(k):
            value,key = heapq.heappop(heap)
            toReturn.append(key)
        return toReturn


        