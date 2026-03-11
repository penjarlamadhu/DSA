class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newarr = []
        for i in nums:
            int_i = int(i)
            newarr.append(i*i)
        return sorted(newarr)