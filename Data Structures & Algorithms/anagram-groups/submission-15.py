class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            newWord = [0]*26
            for letter in word:
                newWord[ord(letter) - ord('a')] += 1
            newWord = tuple(newWord)
            if newWord in hashmap:
                hashmap[newWord].append(word)
            else:
                hashmap[newWord] = [word]
        
        return list(hashmap.values())
