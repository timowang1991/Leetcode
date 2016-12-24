# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
        self.accumNumStr = ''

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)

        return self.sum

    
    def dfs(self, node):
        if node == None:
            return True

        self.accumNumStr += str(node.val)

        leftNodeNone = self.dfs(node.left)
        rightNodeNone = self.dfs(node.right)

        if leftNodeNone and rightNodeNone:
            self.sum += int(self.accumNumStr)

        self.accumNumStr = self.accumNumStr[:-1]

        return False