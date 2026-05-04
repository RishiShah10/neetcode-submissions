class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        map of letters as key for each word
        list of real words as values
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
