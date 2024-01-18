class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = []
#         for s in asteroids:
#             if len(stack)==0:
#                 stack.append(s)
#             elif stack[-1]*s<=0 and s<0:
#                 last_e=stack[-1]
#                 while len(stack)!=0 and stack[-1]*s<=0:
#                     if abs(stack[-1]) == abs(s):
#                         stack.pop()
#                         break
#                     elif abs(stack[-1]) < abs(s):
#                         stack.pop()
#                     else:
#                         break
#                 if abs(last_e) == abs(s):
#                     continue
                    
#                 if len(stack)==0  or abs(last_e) < abs(s):
#                     stack.append(s)
#             else:
#                 stack.append(s)
                    
#         return stack
        # We start by setting up an empty stack.
        stack = []

        # We then go through each asteroid in the array.
        for ast in asteroids:
            # A collision only happens if:
            # There are asteroids in our stack, the current asteroid (ast) is moving left (negative), and the asteroid at the top of the stack is moving right (positive).
            while stack and ast < 0 and stack[-1] > 0:
                # We calculate the result of a collision by comparing the sizes of the two asteroids.
                diff = ast + stack[-1]
                # If the asteroid we're checking (ast) is larger, the smaller one (on the top of the stack) explodes and is removed from the stack.
                if diff < 0:
                    stack.pop()
                # If the asteroid we're checking (ast) is smaller or the same size, it will explode and we stop checking for more collisions.
                elif diff >= 0:
                    ast = 0
                    if diff == 0:
                        stack.pop()
            # If the asteroid (ast) still exists after checking for collisions, we add it to the top of our stack.
            if ast:
                stack.append(ast)

        # Finally, we return the state of the stack, which represents the final state of the asteroid field.
        return stack