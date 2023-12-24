class Solution {
    public int pivotIndex(int[] nums) {
        int sum=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
        }
        int tmp_sum=0;
        for (int i=0;i<nums.length;i++){
            if(tmp_sum==sum-tmp_sum-nums[i])return i;
            tmp_sum+=nums[i];
        }
        return -1;
    }
}