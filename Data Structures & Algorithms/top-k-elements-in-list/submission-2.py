class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        heap = []
        for num in nums:
            freq_map[num] += 1
        for key in freq_map.keys():
            heapq.heappush(heap,(freq_map[key],key))
            if len(heap) > k :
                heapq.heappop(heap)
        result = []
        for i in range(len(heap)):
            neg_count, key = heap[i]
            result.append(key)
        return result


        