# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inOrderTraversal(root, res):
            if root:
                if root.left:
                    inOrderTraversal(root.left, res)
                res.append(root.val)
                if root.right:
                    inOrderTraversal(root.right, res)
        
        inOrderTraversal(root, res)
        return res[k- 1]