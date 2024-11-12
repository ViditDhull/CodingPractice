# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prevval = None
        self.mad = 10**5
        self.traverse(root)
        return self.mad
    def traverse(self, root):
        if not root:
            return None

        self.traverse(root.left)

        if self.prevval is not None:
            self.mad = min(self.mad, abs(root.val - self.prevval))
        self.prevval = root.val
        
        self.traverse(root.right)
