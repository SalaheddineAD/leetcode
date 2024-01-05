class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt=0
        curr_alt=0
        for i in gain:
            curr_alt +=i
            if max_alt<curr_alt:
                max_alt=curr_alt
        return max_alt
