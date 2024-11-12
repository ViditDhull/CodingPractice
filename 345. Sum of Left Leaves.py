# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def calculate(root):
            if not root:
                return 0
            a, b = 0, 0
            if root.left:
                if not root.left.left and not root.left.right:
                    a = root.left.val
                else:
                    a = calculate(root.left)

            if root.right:
                b = calculate(root.right)
            
            return a + b
        
        return calculate(root)
