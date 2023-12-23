class Solution:    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        def getMaxPlants( nb_free_adjacent_plots : int) -> int:
            return max(0, (nb_free_adjacent_plots-2)//2 +(nb_free_adjacent_plots-2)%2)
        
        
        
        list_nb_free_adjacent_plots = []
        list_len = len(flowerbed)
        counter = 0
        for i in range(list_len):
            if flowerbed[i] ==1:
                if (counter >= 3):
                    list_nb_free_adjacent_plots.append(counter)
                counter = 0
            else:
                if i ==0 or i == list_len-1:
                    counter+=1
                counter +=1
                if i == list_len-1:
                    list_nb_free_adjacent_plots.append(counter)
        
        my_list_adjacent_plots = list(map(getMaxPlants, list_nb_free_adjacent_plots))

        free_plantable_plots = sum(list(my_list_adjacent_plots))
        
            
        if list_len==1 and flowerbed[0] == 0:
            free_plantable_plots = 1
        if(free_plantable_plots >= n):
            return True
        else:
            return False