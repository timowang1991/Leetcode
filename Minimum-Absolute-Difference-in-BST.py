# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution(object):
    def __init__(self):
        self.minDiff = sys.maxsize
        self.lastNodeNum = None

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inorderTraverse(root)
        return self.minDiff

    def inorderTraverse(self, node):
        if node == None:
            return

        self.inorderTraverse(node.left)

        if self.lastNodeNum != None:
            self.minDiff = min(self.minDiff, node.val - self.lastNodeNum)
            self.lastNodeNum = node.val
        else:
            self.lastNodeNum = node.val

        self.inorderTraverse(node.right)
