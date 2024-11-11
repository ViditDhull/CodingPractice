# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(start = 0, end = len(nums) - 1):
            if start > end:
                return None

            mid = (start+end)//2
            root = TreeNode(nums[mid])

            root.left = convert(start, mid - 1)
            root.right = convert(mid + 1, end)
            return root
        
        return convert()
