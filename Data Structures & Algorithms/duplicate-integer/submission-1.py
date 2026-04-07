class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i in range(len(nums)):
            if nums[i] not in myMap:
                myMap[nums[i]] = myMap.get(nums[i],0) + 1
            else:
                return True
        return False