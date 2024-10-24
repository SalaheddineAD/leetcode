class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_element = nums[0]
        i=1
        while i < len(nums):
            print(str(i)+", "+str(nums[i])+ ", "+str(last_element))
            if nums[i]==last_element:
                nums.pop(i)
            else:
                last_element = nums[i]
                i+=1

        return len(nums)