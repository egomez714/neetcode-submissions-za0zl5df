class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = 1001
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(nums[l],res)
                break
                # mid = 1 
            mid = (l + r) // 2
            #res = 1
            res = min(nums[mid],res)
            #if 1 >= 1 
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res