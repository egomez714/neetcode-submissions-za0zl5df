class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # cannot use same element twice
        # target = 3 
        left = 0
        right = len(numbers) - 1

        while left < right:
            newTarget = target - numbers[left]
            # 3 - 1 = 2 
            # 1 2 3 4
            # L     R
            if newTarget < numbers[right]:
                right -= 1
            elif newTarget > numbers[right]:
                left += 1
            else:
                return [left+1,right+1]
            




