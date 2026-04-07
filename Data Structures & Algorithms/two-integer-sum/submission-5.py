class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        
        for i in range(len(nums)):
            find = target - nums[i]

            if find not in ans:
                ans[nums[i]] = i
            else:
                return [ans[find], i]
