class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0:
            print("empty string")
            return False
        if len(s)==1 or s[:int(len(s)/2)] == s[::-1][:int(len(s)/2)]:
            return True
        return False
    
    def partition(self, s: str) -> List[List[str]]:
        # Dic: the key is an index of s and the value is a list containing the last index of each palindrom that includes the key as the start. 
        palindromePartitions = {}
        for i in range(len(s)):
            palindromePartitions[i] = [i+1]
        
        # Finding all palindromes
        for window in range(2,len(s)+1):
            for i in range(len(s)-window+1):
                if self.isPalindrome(s[i:i+window]):
                    palindromePartitions[i].append(i+window)
        print(palindromePartitions)
        def extractPalindromes(currIndex: int):
            if currIndex == len(s):
                return [[]]
            final_lists=[]
            for indexEndPalindrome in palindromePartitions[currIndex]:
                # if self.isPalindrome(s[currIndex:indexEndPalindrome]):
                #     print(currIndex,indexEndPalindrome)
                lists= extractPalindromes(indexEndPalindrome)
                print(currIndex)
                print(lists)
                for list in lists:
                    list.insert(0,s[currIndex:indexEndPalindrome])
                    final_lists.append(list)
            return final_lists
        
        return extractPalindromes(0)
