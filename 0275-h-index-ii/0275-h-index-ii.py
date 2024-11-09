class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i,j in enumerate(citations[::-1]):
            if j<i+1:
                return i
        return len(citations)