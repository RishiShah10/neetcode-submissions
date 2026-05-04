class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for n in nums:
            if n in myMap:
                return True
            myMap[n] = 1
        return False