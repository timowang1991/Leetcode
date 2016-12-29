class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [ [0] * (n+1) for _ in xrange(m+1) ]
        for string in strs:
            count = {'0': 0, '1': 0}

            for char in string:
                count[char] += 1

            for i in xrange(m, count['0']-1, -1):
                for j in xrange(n, count['1']-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count['0']][j-count['1']] + 1)

        return dp[m][n]

sol = Solution()
print sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)