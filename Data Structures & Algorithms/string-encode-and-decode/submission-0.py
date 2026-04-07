class Solution:

    def encode(self, strs: List[str]) -> str:
        fullstr = []
        for word in strs:
            fullstr.append(str(len(word)) + ("#") + word)
        return "".join(fullstr)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1 
            wLength = int(s[i:j])
            # 4#NEET wlength = 4
            # i = start of word because j is looking at # 
            i = j + 1
            # j = is looking to end of word
            j = i + wLength 
            # append i up to but not including j (j=next wLength)
            output.append(s[i:j])
            #move i back to length position for next word
            i = j
        return output
