class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels =['a','e','i','o','u','A','E','I','O','U']
        
        result = list(s)
        j=len(result)-1
        print(j)
        #fill the list
        for i in range(len(result)):
            if result[i] in vowels:
                print("i ",i)
                print("1st j ",j)
                while(j>i and result[j] not in vowels):
                    j-=1
                    print("j ",j)
                    
                if (j<=i):
                    return ''.join(e for e in result)
                tmp= result[j]
                result[j]=result[i]
                result[i]=tmp
                j-=1
                
        return ''.join(e for e in result)
                

                
                
                
            
        