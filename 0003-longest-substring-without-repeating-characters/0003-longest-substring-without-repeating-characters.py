class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==1): 
            return 1
        maxlen=0
        first_index=0
        last_index=1
        subString=""
        while(last_index < len(s)):
            subString = s[first_index:last_index]
            index_duplicate = subString.find(s[last_index])
            print("before cleaning: "+s[first_index:last_index+1])
            if(index_duplicate != -1 ):
                first_index = index_duplicate +1 +first_index
            print("after cleaning: "+s[first_index:last_index])
            print()
            if(maxlen < last_index-first_index+1):
                maxlen=last_index-first_index+1
            last_index+=1
        return maxlen