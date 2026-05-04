class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myMapS = defaultdict(int)
        myMapT = defaultdict(int)
        for i in range(len(s)):
            myMapS[s[i]] += 1
            myMapT[t[i]] += 1
        return myMapS == myMapT

        