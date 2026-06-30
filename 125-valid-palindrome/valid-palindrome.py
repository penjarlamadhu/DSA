class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for ch in s:
            if ch.isalnum():
                temp += ch.lower()
        n = len(temp)
        for i in range(n//2):
            if (i >= n//2):
                return True
            if temp[i] != temp[n-i-1]:
                return False
        return True