# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveSearch(self,root:Optional[TreeNode])->List[int]:
        if root == None:
            return []
        if root.right != None:
            right = self.recursiveSearch(root.right)
            print(right)
            if root.left != None:
                left = self.recursiveSearch(root.left)
                if len(left)>len(right):
                    left = left[len(right):]
                    return [root.val] + right +left
            
            return [root.val] + right
                    
        if root.left != None:
            left = self.recursiveSearch(root.left)
            return [root.val] +left
        else:
            return [root.val]

        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.recursiveSearch(root)