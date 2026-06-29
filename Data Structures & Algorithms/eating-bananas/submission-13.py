class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        The speed min is 1 and max the biggest value in the piles
        we bs through possible speeds, try and get the min speed to fit in h hours
        """
        l,r = 1, max(piles)
        def test(h):
            total = 0
            for p in piles:
                total += math.ceil(p/h)
            return total

        while l < r:
            m = (r + l) // 2
            print(m)
            hours_taken = test(m)
            if hours_taken <= h:
                r = m
            elif hours_taken > h:
                l = m + 1

        return l
        