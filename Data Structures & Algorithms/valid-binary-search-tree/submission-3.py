# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validCheck(
            node: Optional[TreeNode],
            lower: float,
            upper:float
        ):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return(
                validCheck(node.left, lower, node.val) and
                validCheck(node.right, node.val, upper)
            )

        return validCheck(root, float("-inf"), float("inf"))
        