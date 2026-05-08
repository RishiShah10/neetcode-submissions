class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix sum array forward pass going through nums each index is numbers multipleid together before 
        suffxi same idea backwards
        '''
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        pc = 1
        sc = 1
        res = []
        for i in range(1,n):
            pc *= nums[i - 1]
            sc *= nums[n - i]
            print(sc)
            prefix[i] = pc
            suffix[n-1-i] = sc
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        
        print(prefix,suffix)
        return res

        