# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorder(self,root,l):
        if not root:
            return None
        self.postorder(root.left,l)
        self.postorder(root.right,l)
        if not root.left and not root.right:
            l.append(root.val)
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leafs1=[]
        leafs2=[]
        self.postorder(root1,leafs1)
        self.postorder(root2,leafs2)
        return all(a==b for a,b in zip(leafs1,leafs2))