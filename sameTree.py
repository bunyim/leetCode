class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def traverse(self, n, m):
        if(n is None and not m is None):
            return False
        if(not n is None and m is None):
            return False
        if(n is None and m is None):
            return True
        if (n.val != m.val):
            return False
        return self.traverse(n.left, m.left) and self.traverse(n.right, m.right)
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.traverse(p, q)