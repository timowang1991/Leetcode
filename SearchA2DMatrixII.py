class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = 0
        y = len(matrix) - 1
        count = 0

        while y >= 0 and x < len(matrix[0]):
            if matrix[y][x] > target:
                y -= 1
            elif matrix[y][x] < target:
                x += 1
            else:
                count += 1
                x += 1
                y -= 1

        return True if count > 0 else False