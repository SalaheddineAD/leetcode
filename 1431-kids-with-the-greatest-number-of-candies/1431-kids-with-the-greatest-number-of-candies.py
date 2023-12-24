class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        index_max = candies.index(max(candies))
        
        for i in range(len(candies)):
            result.append(True if extraCandies+ candies[i]>= candies[index_max] else False)
        return result
                
            