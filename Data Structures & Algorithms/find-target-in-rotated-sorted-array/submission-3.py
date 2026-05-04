class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        ok so lets go l and r
        we want to find target
        so normal binary search and then we need to define conditions
        for moving r,l
        if middle is target return
        1) if left < middle means sorted left side. 
        if target is middle of [l , m] in the sorted so move right to middle - 1
        else middle is in between middle right to left = middle + 1
        2) if left > middle not sorted and if target is in between middle right since
        that is sorted move left to middle + 1
        else move right to middle - 1
        """
        l,r = 0, len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            print(l,m,r)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                


        