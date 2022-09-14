# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def constructABalancedBinaryTree(arr):
            if not arr:
                return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = constructABalancedBinaryTree(arr[:mid])
            root.right = constructABalancedBinaryTree(arr[mid+1:])
            return root

        def inorder(root, sortedArr):
            if root:
                inorder(root.left, sortedArr)
                sortedArr.append(root.val)
                inorder(root.right, sortedArr)
            return sortedArr
        return constructABalancedBinaryTree(inorder(root, []))
