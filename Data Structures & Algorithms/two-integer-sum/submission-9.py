class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            newTarget = target-nums[i]
            if newTarget in hashmap:
                return [hashmap[newTarget],i]
            else:
                hashmap[nums[i]] = i
        