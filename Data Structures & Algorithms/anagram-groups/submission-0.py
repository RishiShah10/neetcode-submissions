class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        map of letters as key for each word
        list of real words as values
        """
        ctwlMap = {}
        for word in strs:
            wordMap = defaultdict(int)
            for char in word:
                wordMap[char] += 1
            key = tuple(sorted(wordMap.items()))
            if key not in ctwlMap:
                ctwlMap[key] = [word]
            else:
                ctwlMap[key].append(word)
        print(ctwlMap)
        return list(ctwlMap.values())
