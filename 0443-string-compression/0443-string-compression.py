class Solution:
    def compress(self, chars: List[str]) -> int:
        def splitNumber(n : int)-> List[int]:
            lst_count =[]
            while(n>=10):
                lst_count.append(n%10)
                print(n%10)
                n = n//10
            lst_count.append(n) 
            print(n)
            return lst_count
        
        chars_input = [i for i in chars]
        chars.clear()
        chars.append(chars_input.pop(0))
        count_last_nb = 1
        
        for e in chars_input:
            if e==chars[-1]:
                count_last_nb +=1
            elif count_last_nb >1:  
                for i in reversed(splitNumber(count_last_nb)):
                    chars.append(str(i))
                count_last_nb = 1
                chars.append(e)
            else:
                chars.append(e)
        if count_last_nb >1:
            for i in reversed(splitNumber(count_last_nb)):
                chars.append(str(i))
        return len(chars)
            
        
        