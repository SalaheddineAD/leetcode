class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j= len(s)-1
        while(i<j):
            val_i = s[i].lower()
            if not((val_i>='a' and val_i<='z') or (val_i>='0' and val_i<='9')):
                i+=1
                continue

            val_j = s[j].lower()
            if not((val_j>='a' and val_j<='z') or (val_j>='0' and val_j<='9')):
                j-=1
                continue
            if val_i != val_j:
                print(f"i = {i}, val_i = {val_i}")
                print(f"j = {j}, val_j = {val_j}")
                return False
            else:
                i+=1
                j-=1
        
        return True
            