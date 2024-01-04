class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # initialization
        max_avg =  sum(nums[:k])/k
        tmp_avg = max_avg

        for i in range(1,len(nums)-k+1):
            tmp_avg = tmp_avg - nums[i-1]/k + nums[i+k-1]/k
            if tmp_avg > max_avg:
                max_avg = tmp_avg
        return max_avg
            