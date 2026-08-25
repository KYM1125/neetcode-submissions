# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        current_level = [root]
        levels = []
        while current_level:
            next_level = []
            levels_val = []
            for node in current_level:
                levels_val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            levels.append(levels_val)
            current_level = next_level
        return levels


        