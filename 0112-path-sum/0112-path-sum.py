# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root ==None:
            return False
        
        def dfs(root, sum:int):
            nonlocal targetSum
            if root.left==None and root.right==None:
                print(sum+root.val)
                if sum+root.val==targetSum:
                    return True
                else:
                    return False
            else:
                if root.left!= None and root.right !=None:
                    return dfs(root.left, sum+root.val) or dfs(root.right, sum+root.val)
            
                if root.right ==None:
                    return dfs(root.left, sum+root.val)
            
                if root.left ==None:
                    return dfs(root.right, sum+root.val)
                
        
        return dfs(root,0)
                        