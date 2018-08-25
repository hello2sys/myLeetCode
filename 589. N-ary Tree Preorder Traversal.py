"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret=[]
        def pre(root,l):
            if not root:
                return
            l.append(root.val)
            for child in root.children:
                pre(child,l)
        pre(root,ret)
        return ret