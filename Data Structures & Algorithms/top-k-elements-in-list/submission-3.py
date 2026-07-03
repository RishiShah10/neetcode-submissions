class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1) Go through nums and create a map of number -> freq
        2) Go through key value in map add to heap (freq,number) sorted on freq
        3) pop k elements return
        """
        myMap = defaultdict(int)
        res = []
        for n in nums:
            myMap[n] += 1
        for num,freq in myMap.items():
            heapq.heappush(res,(freq,num))
            if len(res) > k:
                heapq.heappop(res)
        toreturn = []
        for value in res:
            toreturn.append(value[1])
            
        return toreturn

        