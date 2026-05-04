class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        set up a window
        and go through the string adding chars
        if char not in string move forward like normal adding to 
        max substring counter
        if char is in string move left pointer and reduce map
        """
        window = {}
        ls = 0
        currentS = 0
        left = 0
        right = 0

        while right < len(s):
            char = s[right]
            if char not in window:
                window[char] = right
                ls = max(ls,right - left + 1)
                right += 1
            elif char in window:
                left = max(left, window[char] + 1)
                window[char] = right
                ls = max(ls,right - left + 1)
                right += 1
        return ls

            