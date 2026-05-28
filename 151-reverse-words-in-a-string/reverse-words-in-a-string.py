class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        newstr = ""
        for i in range(len(s)-1,-1,-1):
            newstr += s[i] + " "
        return newstr[:-1]