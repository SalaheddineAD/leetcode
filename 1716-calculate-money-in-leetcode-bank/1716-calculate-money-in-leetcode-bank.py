class Solution:
    def totalMoney(self, n: int) -> int:
        nb_weeks = n//7
        nb_last_days = n%7
        
        money_from_complete_weeks = 28*nb_weeks + nb_weeks*(nb_weeks-1)*7/2
        
        money_from_last_days = (nb_weeks)*nb_last_days + nb_last_days*(nb_last_days+1)/2
        
        return int(money_from_complete_weeks + money_from_last_days)