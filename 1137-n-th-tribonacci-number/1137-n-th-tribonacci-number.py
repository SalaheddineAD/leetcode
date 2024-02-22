class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        ti=0
        ti_1=1
        ti_2=1
        
        if n==0:
            return 0
        if n<3:
            return 1
        
        
        for i in range(n-2):
            tn=ti+ti_1+ti_2
            
            ti, ti_1, ti_2 = ti_1, ti_2, tn
        return tn
            
            