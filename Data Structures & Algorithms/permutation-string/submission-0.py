class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        final = defaultdict(int)
        window = defaultdict(int)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            window[s2[i]] += 1
            final[s1[i]] += 1
        print(final,window)
        if final == window:
            return True
        l,r = 0,len(s1)
        while r < len(s2):
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            window[s2[r]] += 1
            print("MAPS:", final, window)
            if final == window:
                return True
            r += 1
            l += 1

        return False


        