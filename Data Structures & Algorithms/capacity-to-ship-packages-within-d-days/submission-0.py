class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        we need to find the right weight capactiy 
        min is max , max is the sum of weights 
        we can binary search possible vals checking if itll work
        and then return the lowest one
        """
        def getTime(m):
            counter = 1
            currentM = m
            for w in weights:
                if currentM - w < 0:
                    counter += 1
                    currentM = m - w
                else:
                    currentM -= w
            return counter
            

        l,r = max(weights), sum(weights)
        while l < r:
            m = (r + l) // 2
            if getTime(m) > days:
                l = m + 1
            else:
                r = m

        return l