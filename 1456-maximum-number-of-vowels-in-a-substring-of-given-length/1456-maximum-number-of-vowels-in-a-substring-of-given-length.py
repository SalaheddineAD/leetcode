class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        voyels = 'aeiou'
        sub_string = list(s[:k])
        tmp_len=len(list(filter(lambda i: voyels.find(i)!=-1, sub_string)))
        max_len = tmp_len
        
        for i in s[k:]:
            sub_string.append(i)
            if voyels.find(i) !=-1:
                tmp_len+=1
                
            if voyels.find(sub_string.pop(0)) != -1:
                tmp_len = max(0,tmp_len-1)
                
            if tmp_len>max_len:
                max_len = tmp_len
                
        return max_len
            