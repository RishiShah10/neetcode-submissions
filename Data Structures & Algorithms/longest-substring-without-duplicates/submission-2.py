class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        go through string keeping a map of the chars
        if char in it remove the char starting from l until its gone
        """
        myMap = {}
        l,r = 0,0
        longest = 0
        while r < len(s):
            while s[r] in myMap:
                del myMap[s[l]]
                l += 1
            print(r,l)
            myMap[s[r]] = 1
            longest = max(longest, r - l + 1)
            r += 1
            
        return longest
        