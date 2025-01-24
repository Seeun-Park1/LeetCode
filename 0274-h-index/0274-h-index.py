class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i in range(n, -1, -1): 
            ind = bisect_left(citations, i)
            if n - ind >= i: return i  