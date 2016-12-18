class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        pathTable = [[1]*n] + [[0]*n for _ in xrange(m-1)]
        for x in pathTable:
            x[0] = 1

        for x in xrange(1,m):
            for y in xrange(1,n):
                pathTable[x][y] = pathTable[x-1][y] + pathTable[x][y-1]

        return pathTable[m-1][n-1]

sol = Solution()
print sol.uniquePaths(3, 3)