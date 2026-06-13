class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given array of strings
        # find same freq of string
        # any order for output

        # use hashmap
        # find freq of string
        # may freq : [string]
        # return list(map.values())


        freqHolder = {}
        
        for word in strs:
            freq = [0]*26

            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            if tuple(freq) not in freqHolder:
                freqHolder[tuple(freq)] = []
            
            freqHolder[tuple(freq)].append(word)
        return list(freqHolder.values())





        