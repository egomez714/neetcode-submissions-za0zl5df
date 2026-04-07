class Solution:

    def encode(self, strs: List[str]) -> str:
        ans =""
        for word in strs:
            ans += str(len(word)) + '#' + word
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        # traverses entire string
        while i < len(s):
            # string = n#word starts from first char
            j = i
            # stops at '#' to get the entire number
            while s[j] != '#' and j < len(s):
                j += 1
            #uses splice to store length
            length = int(s[i:j])
            #moves i to the start of word 
            i = j + 1
            #starting from i end at length of word and
            #j which is where prev word started + 1 to account for #
            currentWord = s[i:length+j+1]
            res.append(currentWord)
            #saves i at after currentword is stored starts at next word
            i += length
        return res         
