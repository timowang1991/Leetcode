class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for x in xrange(0, len(words)):
            rowWord = words[x][x:]
            colWord = ''

            try:
                for y in xrange(x, len(words)):
                    colWord += words[y][x]
            except Exception as e:
                if rowWord != colWord:
                    return False
                continue

            if rowWord != colWord:
                return False

        return True

sol = Solution()
print sol.validWordSquare([
    "abcd",
    "bnrt",
    "crm",
    "dt"])