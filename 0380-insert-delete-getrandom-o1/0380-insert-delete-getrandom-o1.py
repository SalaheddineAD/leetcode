import random
class RandomizedSet:

    def __init__(self):
        self.lst =[]
        self.len = 0

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False
        else:
            self.lst.insert(random.randint(0, self.len), val)
            self.len+=1
            return True
            
    def remove(self, val: int) -> bool:
        if val not in self.lst:
            return False
        else:
            self.lst.remove(val)
            self.len-=1
            return True
        
    def getRandom(self) -> int:
        return self.lst[random.randint(0, self.len-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()