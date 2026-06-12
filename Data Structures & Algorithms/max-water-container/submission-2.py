class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0, len(heights) - 1
        maximumAreaFound = 0
        while left < right:
            area = (right - left) * min(heights[left],heights[right])

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                
            maximumAreaFound = max(area,maximumAreaFound)

        return maximumAreaFound
