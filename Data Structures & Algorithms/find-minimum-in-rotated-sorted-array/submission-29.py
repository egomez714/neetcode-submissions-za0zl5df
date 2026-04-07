class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        lowest = nums[0]
        while l < r:
            if nums[l] < nums[r]:
                lowest = min(nums[l],lowest)
                break
            mid = l + r +1 // 2
            # 1 >= 1
            if nums[mid] >= nums[l]:
                lowest = min(lowest,nums[l])
                l = mid + 1
                
            if nums[mid] >= nums[r]:
                lowest = min(lowest,nums[r])
                r = mid - 1
                
        # 2 1
        # 0 1   
        # l r
        return lowest