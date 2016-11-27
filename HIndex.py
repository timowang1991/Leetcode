class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        hIdx = 0

        for i, citation in enumerate(citations):
            h = len(citations) - i

            if citation >= h:
                hIdx = max(hIdx, h)

        return hIdx

sol = Solution()
# print sol.hIndex([3, 0, 6, 1, 5])
print sol.hIndex([1])