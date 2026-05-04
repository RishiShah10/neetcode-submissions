class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        biggestSequence = 0
        for i in range(len(nums)):
            counter = 0
            current = nums[i]
            print(current)
            if current - 1 not in seen:
                while current in seen:
                    current += 1
                    counter += 1
                biggestSequence = max(biggestSequence, counter)
        return biggestSequence

            
        