class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix array all numbers before it multipled
        sufix array all numbers after multipled
        go through both and then find multiply number
        """
        n = len(nums)
        result = []
        prev = 1
        for a in nums:
            result.append(prev)
            prev *= a
        suff = 1
        print(result)
        for i in range(n-1,-1,-1):
            result[i] *= suff
            suff *= nums[i]

        return result
