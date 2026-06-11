class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evencount = 0
        for i in (nums):
            digitcount = 0
            for j in str(i) :
                digitcount +=1
            if digitcount % 2 ==0 :
                evencount +=1 
        return evencount