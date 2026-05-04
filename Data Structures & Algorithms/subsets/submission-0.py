class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        # pick and go to next dont pick and go recusrive type of loop
        def dfs(i):
            #reached end of list so add
            if i >= len(nums):
                res.append(subset.copy())
                return
            #pick
            subset.append(nums[i])
            dfs(i + 1)
            #dont pick
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res