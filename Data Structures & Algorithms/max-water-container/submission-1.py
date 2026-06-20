class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Start L and R at oppisite ends
        calc max water move lower height until they reach
        """
        l,r = 0,len(heights) - 1
        maxWater = 0
        while l < r:
            minHeight = min(heights[l],heights[r])
            currentWater = (r - l) * minHeight
            maxWater = max(maxWater,currentWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater


        