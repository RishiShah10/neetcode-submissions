class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Make a heap and keep k size. pop the k elements after
        """
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        return heap[0]
