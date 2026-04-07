class Solution:
    

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for word in strs:
            wordFreq = tuple(self.freq(word))
            ans[wordFreq].append(word)
        return list(ans.values())

    @staticmethod
    def freq (s):
        arr = [0] * 26
        for i in range(len(s)):
            ch = s[i]
            index = ord(ch) - ord('a')
            arr[index] += 1
        return arr
        