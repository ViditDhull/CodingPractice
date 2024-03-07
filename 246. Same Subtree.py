# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return '  '
            
            l = dfs(node.left)
            r = dfs(node.right)

            return f' {node.val} {l} {r} '
        return dfs(subRoot) in dfs(root)