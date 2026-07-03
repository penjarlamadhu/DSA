class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = {}
        for i, num in enumerate(nums):
            need = target - num 
            if need in new :
                return new[need],i 
            new[num] = i

        #two pointers