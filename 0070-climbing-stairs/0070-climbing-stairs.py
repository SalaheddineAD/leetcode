class Solution:
    def factorial(self, n:int)-> int:
        if n==1 or n==0:
            return 1
        else:
            return n*self.factorial(n-1)
        
        
    def climbStairs(self, n: int) -> int:
        sum=0
        for nb_2 in range(int(n/2)+1):
            nb_1 = n-nb_2*2
            combinaisons = factorial(nb_1+nb_2)/(self.factorial(nb_1)*self.factorial(nb_2))
            # print(nb_1, "  ", nb_2)
            # print(combinaisons)
            sum+= combinaisons
            
        return int(sum)