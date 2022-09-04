# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def fun(root, count, levelDict, depth):
            if root:
                fun(root.right, count+1, levelDict, depth+1)
                if count in levelDict.keys():
                    levelDict[count].append([root.val, depth])
                else:
                    levelDict[count] = [[root.val, depth]]
                fun(root.left, count-1, levelDict, depth+1)
            return levelDict
        res = []
        for item in OrderedDict(sorted(fun(root, 1, {}, 0).items())).values():
            if len(item) > 1:
                level = []
                item.sort(key=lambda x: (x[1], x[0]))
                res.append([i[0] for i in item])
            else:
                res.append([item[0][0]])
        return res
