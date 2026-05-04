class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        go from ends move if smaller length then other keep going
        """
        n = len(heights)
        l,r = 0, n - 1
        best = 0
        while l < r:
            best = max(best, min(heights[l],heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1

        return best
