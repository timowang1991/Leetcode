# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.paths = []
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.traversal(root)
        return self.paths
        
    def traversal(self, node, path = []):
        if node == None:
            return

        path.append(str(node.val))

        self.traversal(node.left, path)
        self.traversal(node.right, path)

        if node.left == None and node.right == None:
            self.paths.append('->'.join(path))

        path.pop()