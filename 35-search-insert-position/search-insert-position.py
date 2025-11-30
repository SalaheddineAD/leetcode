class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        size = len(nums)
        step = int(size/2)
        pos = int(size/2)

        if size ==1:
            return 0 if target<=nums[0] else 1

        while step>=1:
            print(f"pos = {pos}")
            if nums[pos] == target:
                return pos
            pos = min(pos +step,size-1) if target>nums[pos] else max(pos-step,0)
            print(f"step = {step}")
            step = int(step/2)

        if nums[size-1]<target:
            return size
        if nums[pos]<target:
            return pos+1
        return pos
