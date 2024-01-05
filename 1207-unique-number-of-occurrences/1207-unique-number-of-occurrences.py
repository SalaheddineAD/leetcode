class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        # print(dic.values())
        if len(dic.values())==len(set(dic.values())):
            return True
        else:
            return False