class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in ans:
                return [ans[find], i]
            else:
                ans[nums[i]] = i