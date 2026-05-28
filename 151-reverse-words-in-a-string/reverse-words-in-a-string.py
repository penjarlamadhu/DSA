class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        newstr = []
        for i in range(len(s)-1,-1,-1):
            newstr.append(s[i])
        return " ".join(newstr)