class Solution:
       
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations ="/*+-"
        
        for c in tokens:
            if c in operations:
                b = stack.pop()
                a = stack.pop()
                
                match c:
                    case "+":
                        c = a+b
                    case "-":
                        c =a-b
                    case "*":
                        c= a*b
                    case "/":
                        c= a/b
                    case "_":
                        c=0
            stack.append(int(c))
        return stack.pop()
                    