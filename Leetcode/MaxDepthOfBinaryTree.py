# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def fun(root, depth):
            if root == None:
                return depth
            depth = max(depth, fun(root.left, depth+1),
                        fun(root.right, depth+1))
            return depth
        return fun(root, 0)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def levelOrder(root: TreeNode) -> List[List[int]]:
            result = []

            if root == None:
                return result

            Queue = []
            Queue.append(root)

            while len(Queue):
                size = len(Queue)
                currentLevel = []
                for i in range(size):
                    current = Queue.pop()
                    currentLevel.append(current.val)
                    if current.left != None:
                        Queue.insert(0, current.left)
                    if current.right != None:
                        Queue.insert(0, current.right)
                if currentLevel != []:
                    result.append(currentLevel)
            return result
        return len(levelOrder(root))
