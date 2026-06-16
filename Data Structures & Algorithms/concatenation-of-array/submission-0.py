class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # int arr nums
        # return int arr size 2 * len(nums)

        newArr= [0] * len(nums) * 2
        for i in range(len(newArr)):
            newArr[i] = nums[i % len(nums)]
            
        return newArr