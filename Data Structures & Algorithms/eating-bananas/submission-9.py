class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k can either be min of 0 or max of the biggest value in piles right 
        so range is 0 to max(piles)
        choose bs value test it if valid good, store keep testing then replacing result with min result
        """
        l = 1
        r = max(piles)
        def test(m,h):
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)
            return (time <= h)

        while l <= r:
            m = (r + l) // 2
            if (test(m,h)):
                r = m - 1
            else:
                l = m + 1
        return l


        