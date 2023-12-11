class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int median;
        int m = nums1.length;
        int n = nums2.length;
        if (n == 0 &&m==0)return 0.0;
        else if(n==0){
            if(m%2==0)return  (double)(nums1[(m)/2-1]+nums1[m/2])/2;
            else return nums1[m/2];
        }
        else if(m==0){
            if(n%2==0) return (double)(nums2[n/2-1]+nums2[n/2])/2;
            else return nums2[n/2];
        }
        median =((n + m)%2==0 )?  (n+m)/2-1 : (n+m)/2;
        int i=0;
        int j=0;
        int k=0;
        double median_value=0;
        while(k<=median){
            if(i>=m){
                System.out.println(i);
                if((n+m)%2==0)
                    return (double)(nums2[(n+m)/2-m-1]+nums2[(n+m)/2-m])/2;
                else return (double)nums2[(n+m)/2-m];
                // if(m%2==0) return nums2[(n-j-m)/2];
                // else return nums2[(n-j-m)/2];
            }
            else if(j>=n){
                System.out.println("k");
                if((n+m)%2==0)
                    return (double)(nums1[(n+m)/2-n-1]+nums1[(n+m)/2-n])/2;
                else return nums1[(n+m)/2-n];
            }
            else if(nums1[i]<=nums2[j]){
                median_value=nums1[i];
                i++;
            }
            else {
                median_value=nums2[j];
                j++;
            }
            k++;
        }
        System.out.println(i);
        if((n + m)%2==0) {
            if(j>=n)median_value+=nums1[i];
            else if(i>=m)
                median_value+=nums2[j];
            else if(nums1[i]<=nums2[j])
                median_value+=nums1[i];
            else
                median_value+=nums2[j];
            median_value/=2;
        }
        return median_value;
    }
}