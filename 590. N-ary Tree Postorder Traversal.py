"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret=[]
        def post(root,l):
            if not root:
                return
            for child in root.children:
                post(child,l)
            l.append(root.val)
        post(root,ret)
        return ret