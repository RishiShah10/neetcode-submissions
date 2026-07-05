class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def test(m):
            currH = 0
            for pile in piles:
                currH += math.ceil(pile/m)
            return currH
        l,r = 1,max(piles)
        while l <= r:
            m = (l + r)//2
            testH = test(m)
            if testH > h:
                l = m + 1
            else:
                r = m - 1
        return l
        
        