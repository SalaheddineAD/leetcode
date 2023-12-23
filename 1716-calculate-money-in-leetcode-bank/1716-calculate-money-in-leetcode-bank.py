class Solution:
    def totalMoney(self, n: int) -> int:
        nb_weeks = n//7
        nb_days_in_last_week = n%7
        total=0
        for i in range(nb_weeks):
            total += (7+i)*(7+1+i)/2 - i*(i+1)/2
        
        total += (nb_days_in_last_week+nb_weeks)*(nb_days_in_last_week +nb_weeks 
                                                  +1)/2 - (nb_weeks*(nb_weeks+1)/2)
        return int(total)