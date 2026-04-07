class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i in range(len(nums)):
            find = target - nums[i]
            if find in myDict:
                return [myDict[find],i]
            else:
                myDict[nums[i]] = i