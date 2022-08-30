"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def solve(root, res):
            if root.children == []:
                return [root.val]
            for node in root.children:
                solve(node, res)
                res.append(node.val)
            return res + [root.val]
        return solve(root, []) if root else []