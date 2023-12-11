class Solution:
    def reverse(self, x: int) -> int:
        output=0
        isNegatif=1
        if(x<0):
            isNegatif = -1
            x=-x
        while x>=10:
            output=output*10
            output += x%10
            x=int(x/10)

        if x !=0:
            output=output*10
            output += x%10

        if output>pow(2,31)-1:   
            return 0
            
        return output*isNegatif
