class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        make prefix sums of the values of everything to the left, multiplied
        make prefix sum of everything to the right multiplied
        return list is [everything to left * everything to right of it multiplied... for all values]
        """
        n  = len(nums)
        prefixL = [1] * n
        runningL = 1
        prefixR = [1] * n
        runningR = 1
        runningR
        for i in range(n):
            prefixL[i] = runningL
            runningL *= nums[i]
            prefixR[n - i - 1] = runningR
            runningR *= nums[n - i - 1]
        for i in range(n):
            prefixL[i] *= prefixR[i]
            

        return prefixL