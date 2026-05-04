class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        i guess we could make two prefix sum arrays so everythigng multipled starting from left 
        and one starting from the right
        then we could go point by point and multiply them by each other 
        """
        n = len(nums)
        preL = [1] * n 
        preR = [1] * n
        l,r = 1,1
        result = []
        for i in range(0,len(nums)):
            preL[i] = l
            preR[i] = r
            l *= nums[i]
            r *= nums[n - 1 -  i]
        print(preL,preR)
        for i in range(0,n):
            value = preL[i] * preR[n - 1 - i]
            result.append(value)
            print(result)


        return result