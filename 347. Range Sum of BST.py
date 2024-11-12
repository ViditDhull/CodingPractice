# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root, high, low):
            if not root:
                return 0
            a = b = c = 0

            if root.val <= high and root.val >= low:
                c = root.val
            if root.val < high:
                a = dfs(root.right, high, low)
            if root.val > low:
                b = dfs(root.left, high, low)
            

            return a + b + c
        return dfs(root, high, low)
