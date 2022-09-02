# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        return [sum(level)/len(level) for level in levelOrder(root)]