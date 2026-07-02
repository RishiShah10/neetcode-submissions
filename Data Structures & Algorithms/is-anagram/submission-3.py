class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        if len(s) != len(t):
            return False
        n = len(s)
        for i in range(n):
            s_map[s[i]] += 1
            t_map[t[i]] += 1
        return s_map == t_map