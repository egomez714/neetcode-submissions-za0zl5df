class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        shortest = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                shortest = min(nums[l],shortest) 
                break
            mid = (l + r) // 2
            shortest = min(shortest,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return shortest