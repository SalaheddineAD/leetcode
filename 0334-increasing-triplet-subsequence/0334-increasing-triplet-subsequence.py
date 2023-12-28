class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        small = sys.maxsize
        medium = sys.maxsize
        
        for big in nums:
            if big <= small:
                small = big
            elif big <= medium:
                medium = big
            else:
                return True
        return False
            