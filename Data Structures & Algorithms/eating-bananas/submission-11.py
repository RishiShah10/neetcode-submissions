class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        if hrs < len(list):: return false
        ok so we know that the fastest speed one can eat is the biggest of the 
        list cause u can only finish one pile max an hour yk

        so anwser is from 1 to max(piles)
        binary search test it till we get lowest possible anwser
        """
        if h < len(piles): return -1
        l,r = 1,max(piles)
        def test(m):
            testHours = 0 
            for p in piles:
                testHours += math.ceil(p/m)
            return testHours
        while l < r:
            m = (r + l) // 2
            testHours = test(m)
            if testHours > h:
                l = m + 1
            else:
                r = m
        


        return l

        