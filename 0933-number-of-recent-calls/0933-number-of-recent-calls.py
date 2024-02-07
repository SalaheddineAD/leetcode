class RecentCounter:

    def __init__(self):
        self.counter=3000
        self.len=0
        self.requests=[]
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        counter=0
        self.len+=1
        i= self.len-1
        last_time= self.requests[i]-3000
        
        while self.requests[i]>=last_time:
            counter+=1
            i-=1
            # print(counter)
            if i<0:
                break
        return counter
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)