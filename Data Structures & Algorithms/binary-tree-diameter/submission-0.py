# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        dia=0
        def maxDepth(root):
            if not root:
                return 0
            nonlocal dia
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            dia=max(dia,left_depth+right_depth)
            return max(left_depth, right_depth) + 1
        maxDepth(root)
        return dia    