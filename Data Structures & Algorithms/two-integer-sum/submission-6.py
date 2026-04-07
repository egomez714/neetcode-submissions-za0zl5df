class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict(int)
        for i in range(len(nums)):
            find = target - nums[i]
            if find in m:
                return [m[find], i]
            else:
                m[nums[i]] = i