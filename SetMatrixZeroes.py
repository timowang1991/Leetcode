class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        firstColZero = False

        for row in xrange(0, len(matrix)):
            if matrix[row][0] == 0:
                firstColZero = True
                break

        for col in xrange(0, len(matrix[0])):
            if matrix[0][col] == 0:
                firstRowZero = True
                break

        # Record any zero element within the matrix on the first element of its row and col
        for row in xrange(1, len(matrix)):
            for col in xrange(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in xrange(1, len(matrix)):
            if matrix[row][0] != 0:
                continue
            for col in xrange(1, len(matrix[row])):
                matrix[row][col] = 0

        for col in xrange(1, len(matrix[0])):
            if matrix[0][col] != 0:
                continue
            for row in xrange(1, len(matrix)):
                matrix[row][col] = 0

        if firstRowZero:
            for col in xrange(0, len(matrix[0])):
                matrix[0][col] = 0

        if firstColZero:
            for row in xrange(0, len(matrix)):
                matrix[row][0] = 0