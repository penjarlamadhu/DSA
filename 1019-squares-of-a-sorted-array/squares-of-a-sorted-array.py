import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        result = [0] * n
        l = 0
        r = n-1
        pop = n-1
        while(l <= r):   
            if abs(nums[l]) > abs(nums[r]):
                result[pop] = nums[l] * nums[l]
                l+=1
            else:
                result[pop] = nums[r] * nums[r]
                r-=1
            pop -= 1
        return result