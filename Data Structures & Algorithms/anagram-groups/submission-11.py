class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for i in range(len(strs)):
            word = self.helper(strs[i])
            if word in myDict:
                myDict[word].append(strs[i])
            else:
                myDict[word] = [strs[i]]
            

        return list(myDict.values())
    def helper(self,s)-> str:
        arr = [0]*26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
        return tuple(arr)