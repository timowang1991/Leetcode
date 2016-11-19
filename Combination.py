class Solution(object):
    def __init__(self):
        self.combinations = []
        self.levelLimit = 0

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.levelLimit = k
        self.recursive(1, n)

        return self.combinations
    
    def recursive(self, begin, end, level = 1, combination = []):
        if begin > end or level > self.levelLimit:
            if len(combination) == self.levelLimit:
                self.combinations.append(combination[:])
            return

        for x in xrange(begin, end + 1):
            combination.append(x)
            self.recursive(x + 1, end, level + 1, combination)
            combination.pop()

sol = Solution()
print sol.combine(4, 2)