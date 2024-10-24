class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return
        i = 2
        last_el= nums[1]
        last_el2=nums[0]
        
        while i< len(nums):
            
            if last_el != last_el2 or last_el!= nums[i]:
                last_el2 = last_el
                last_el = nums[i]
                i+=1
            else:
                nums.pop(i)
        return len(nums)
                
                
                
