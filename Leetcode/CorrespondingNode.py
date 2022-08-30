class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned == None or cloned.val == target.val:
            return cloned
        node = self.getTargetCopy(original, cloned.left, target)
        if node != None:
            return node
        return self.getTargetCopy(original, cloned.right, target)