# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def find_depth(root, depth):
            if not root:
                return depth
            depth += 1
            return max(find_depth(root.left, depth), find_depth(root.right, depth))

        return find_depth(root, 0)
