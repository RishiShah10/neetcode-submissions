class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix array all numbers before it multipled
        sufix array all numbers after multipled
        go through both and then find multiply number
        """
        n = len(nums)
        prefix = [1] *(n)
        suffix = [1] * (n)
        result = []
        for i in range(1,n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for j in range(1,n):
                suffix[j] = suffix[j - 1] * nums[n - j]
        print(prefix,suffix)
        for k in range(n):
            result.append(prefix[k] * suffix[n - k - 1])
        return result
