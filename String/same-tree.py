class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # both nodes are None, trees are the same
            return True
        elif not p or not q:  # one node is None, trees are not the same
            return False
        elif p.val != q.val:  # nodes have different values, trees are not the same
            return False
        else:
            # recursively check left and right subtrees
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)