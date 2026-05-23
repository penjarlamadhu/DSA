class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        arr = [""]* len(words)
        for word in words :
            position = int(word[-1])-1
            arr[position] = word[:-1]
        return " ".join(arr)