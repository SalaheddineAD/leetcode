# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums=[0]
        
        def recursive(node:Optional[TreeNode],level):
            if node != None:
                if len(sums)<level+1:
                    sums.append(node.val)
                else:
                    sums[level] +=node.val
                recursive(node.right,level+1)
                recursive(node.left,level+1)
                
        recursive(root,0)
        print(sums)
        max_index=0
        
        for i in range(len(sums)):
            if sums[i] >sums[max_index]:
                max_index= i
        
        return max_index+1
                