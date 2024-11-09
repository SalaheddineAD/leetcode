import random
class RandomizedSet:

    def __init__(self):
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic.keys():
            return False
        else:
            self.dic[val] = 1
            return True
            
    def remove(self, val: int) -> bool:
        if val not in self.dic.keys():
            return False
        else:
            del self.dic[val]
            return True
        
    def getRandom(self) -> int:
        return random.choice(list(self.dic.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()