"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        seq,ret=[root],[]
        while seq:
            tmp,tmp_ret=[],[]
            tmp.extend(seq)
            seq=[]
            while tmp:
                top=tmp.pop(0)
                tmp_ret.append(top.val)
                for child in top.children:
                    seq.append(child)
            ret.append(tmp_ret)
        return ret