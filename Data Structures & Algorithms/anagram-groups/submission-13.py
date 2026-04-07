class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            parsedWord = self.createAnagram(word)
            if parsedWord in res:
                res[parsedWord].append(word)
            else:
                res[parsedWord] = [word]
        return list(res.values())
    def createAnagram(self,word):
        arr = [0]*26
        for c in word:
            num = ord(c) - ord('a')
            arr[num] += 1
        return tuple(arr)

