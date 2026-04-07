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
            i = j + 1
            word = s[i:length+j+1]
            res.append(word)
            i += length
        return res         
