class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.split()
        n = len(li[-1])
        return n 
        