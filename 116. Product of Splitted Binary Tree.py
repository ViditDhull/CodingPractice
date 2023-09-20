# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        O(n) O(n) | n = node count
        """
        cusums = []
        def cusum(n: Optional[TreeNode]):
            if not n: return 0
            cusums.append(n.val + cusum(n.left) + cusum(n.right))
            return cusums[-1]
        cusum(root)
        return max((cusums[-1] - s) * s for s in cusums) % 1_000_000_007