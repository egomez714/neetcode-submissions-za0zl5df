class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        mySet = set(nums)
        for num in mySet:
            if (num-1) not in mySet:
                length = 1
                while (num+length) in mySet:
                    length+=1
                longest = max(length,longest)
        return longest