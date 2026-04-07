class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
        water = 0
        while l  <= r:
            if maxL < maxR:
                if maxL - height[l] <= 0:
                    maxL = max(maxL,height[l])
                    l += 1
                else:
                    water += maxL-height[l]
                    maxL = max(maxL,height[l]) 
                    l+= 1
            else:
                if maxR - height[r] <= 0:
                    maxR = max(maxR,height[r])
                    r-=1
                else:
                    water+= maxR-height[r]
                    maxR=max(maxR,height[r])
                    r-=1
        return water