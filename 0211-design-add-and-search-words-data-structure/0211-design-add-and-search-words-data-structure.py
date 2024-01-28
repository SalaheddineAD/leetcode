class DicNode:
    def __init__(self):
        self.children ={}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = DicNode()

        
    def helperSearch(self,word:str, root):
        curr = root
        for i in range(len(word)):
            c= word[i]
            if word[i] == '.':
                result = False
                if len(curr.children.keys())==0:
                    return result
                
                for k in curr.children.values():
                    result = result or self.helperSearch(word[i+1:], k)
                return result
            
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.endOfWord
        # return True
        
    def search(self, word: str) -> bool:

        return self.helperSearch(word, self.root)
         

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]= DicNode()
            curr  = curr.children[c]
        curr.endOfWord = True
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)