"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        Q = [root]
        res = [[root.val]]
        while len(Q):
            level = []
            for i in range(len(Q)):
                node = Q.pop(0)
                for child in node.children:
                    level.append(child.val)
                    Q.append(child)
            if level != []:
                res.append(level)
        return res
