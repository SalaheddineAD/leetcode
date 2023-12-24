import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #find the commun deviders of len(str1) and len(str2)
        # then check if str1 and str2 are multiples of str[0:devider]
        # you go from the longest to the shortest and if none of them is there #is non
    
        len1 = len(str1)
        len2 = len(str2)
        
        def isGcd(i:int) -> bool:
            
            if len1%i!=0 or len2%i!=0:
                return False
            # print(str1[0:i]*(len1//i))
            if str1 ==str1[0:i]*(len1//i) and str2 == str1[0:i]*(len2//i):
                return True
            return False
        
        if isGcd(min(len1,len2)):
            return str1[0:min(len1,len2)]
        
        for i in range(int((min(len1,len2))),0,-1):
            if isGcd(i):
                return str1[0:i]
        
        return ""
                       
                       
            