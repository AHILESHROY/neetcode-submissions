class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both nodes are None -> Structural Match
        if not p and not q:
            return True
            
        # Base Case 2: One node is missing, or values don't match -> Failure
        if not p or not q or p.val != q.val:
            return False
            
        # Recursive Case: Check if both left and right subtrees match perfectly
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
