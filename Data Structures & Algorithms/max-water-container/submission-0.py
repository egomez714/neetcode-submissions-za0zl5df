class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        start = 0
        finish = len(heights)-1
        maxSpace = 0
        while (start < finish):
            area = min(heights[start], heights[finish]) * (finish - start)
            maxArea = max(maxArea, area)
            left = heights[start]
            right = heights[finish]
            if left > right:
                finish -= 1
            else:
                start += 1
        return maxArea
