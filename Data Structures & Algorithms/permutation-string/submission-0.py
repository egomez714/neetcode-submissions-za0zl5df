class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        myMapOne = [0] * 26
        myMapTwo = [0] * 26
        for i in range (len(s1)):
            myMapOne[ord(s1[i]) - ord('a')] += 1
            myMapTwo[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if myMapOne[i] == myMapTwo[i] else 0)
        l = 0
        for r in range (len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            myMapTwo[index] += 1
            if myMapOne[index] == myMapTwo[index]:
                matches +=1
            elif myMapOne[index] + 1 == myMapTwo[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            myMapTwo[index] -= 1
            if myMapOne[index] == myMapTwo[index]:
                matches +=1
            elif myMapOne[index] - 1 == myMapTwo[index]:
                matches -= 1
            l+=1
        return matches == 26
            