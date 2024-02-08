class RecentCounter:

    def __init__(self):
        self.count=0
        self.requests=deque()
        
    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.count+=1
        
        last_time= t-3000
        
        while self.requests[0]<last_time:
            self.count-=1
            self.requests.popleft()

        return self.count
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)