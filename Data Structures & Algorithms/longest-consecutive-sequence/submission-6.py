class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        i = 0
        mySet = set(nums)
        longest = 0
        while i < len(nums):
            if nums[i] in mySet:
                target = nums[i]
                long = 0
                while target in mySet:
                    target+=1
                    long+= 1
            i+=1
            longest = max(long,longest)
        return longest
