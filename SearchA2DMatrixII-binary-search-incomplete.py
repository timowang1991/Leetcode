class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.x1, self.y1 = (0, 0)
        self.x2, self.y2 = (len(matrix[0]) - 1, len(matrix) - 1)
        self.matrix = matrix
        self.target = target

    def findTargetInFirstRow(self):
        x1 = self.x1
        x2 = self.x2
        firstRow = self.matrix[self.y1]

        if firstRow[x1] == self.target or firstRow[x2] == self.target:
            return True
        elif firstRow[x2] < self.target:
            return False

        while x2 - x1 <= 1:
            midIdx = (x1 + x2) / 2
            if firstRow[midIdx] == self.target:
                return True
            elif firstRow[midIdx] < self.target:
                x1 = midIdx
            elif firstRow[midIdx] > self.target:
                x2 = midIdx

        self.x2 = x2 if firstRow[x2] < self.target else x1
        return False

    def findTargetInFirstCol(self):
        y1 = self.y1
        y2 = self.y2

        if self.matrix[y1][self.x1] == self.target or self.matrix[y2][self.x1] == self.target:
            return True
        elif self.matrix[y2][self.x1] < self.target
            return False