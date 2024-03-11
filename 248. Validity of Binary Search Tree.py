# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def inOrderTraversal(root, res):
            if root:
                if root.left:
                    inOrderTraversal(root.left, res)
                res.append(root.val)
                if root.right:
                    inOrderTraversal(root.right, res)
        inOrderTraversal(root, res)
        if len(res) < 2:
            return True
        p = 0
        while p < len(res) - 1:
            if res[p] >= res[p+1]:
                return False
            else:
                p += 1
        return True