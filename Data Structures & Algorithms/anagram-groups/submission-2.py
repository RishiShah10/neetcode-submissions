class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create a map for every word representing all chars
        make a map of map and list of words append to that
        cant use map as a key though hmm
        can make a list of 26 and turn every char into 0,1,2 in alphabet
        turn that list to a tuple make a map of 
        tuple -> list of words return the values
        """
        myMap = defaultdict(list)
        for word in strs:
            charList = [0] * 26
            for char in word:
                positionInAlphabet = ord(char) - ord('a')
                charList[positionInAlphabet] += 1
            myMap[(tuple(charList))].append(word)
        return list(myMap.values())
        