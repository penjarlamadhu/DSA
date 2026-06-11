class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lenarr = len(nums)
        sets = set(nums)
        lenset = len(sets)
        if lenarr != lenset :
            return True
        else:
            return False