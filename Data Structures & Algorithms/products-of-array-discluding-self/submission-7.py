class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix array all numbers before it multipled
        sufix array all numbers after multipled
        go through both and then find multiply number
        """
        n = len(nums)
        result = [1] * n
        prev = 1
        for i in range(n):
            result[i] *= prev
            prev *= nums[i]
        suff = 1
        for i in range(n-1,-1,-1):
            result[i] *= suff
            suff *= nums[i]


        return result
