# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        def dfs(node, n):
            n += node.val

            if not node.left and not node.right:
                return n>= limit
            
            l = dfs(node.left, n) if node.left else False
            r = dfs(node.right, n) if node.right else False

            if not l: node.left = None
            if not r: node.right = None

            return l or r

        return root if dfs(root, 0) else None