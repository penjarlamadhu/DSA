class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0 
        rp = len(height) -1 
        maxwater = 0 
        while (lp < rp ):
            w = rp-lp
            ht = min(height[lp], height[rp])
            currentwater = w * ht 
            maxwater = max(maxwater, currentwater)

            if height[lp] < height[rp]:
                lp +=1 
            else:
                rp -=1
        return maxwater
