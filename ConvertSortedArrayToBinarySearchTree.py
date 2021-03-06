# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        return self.convertToBST(nums, 0, len(nums) - 1)

    def convertToBST(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end)/2
        root = TreeNode(nums[mid])

        root.left = self.convertToBST(nums, start, mid - 1)
        root.right = self.convertToBST(nums, mid + 1, end)
        return root