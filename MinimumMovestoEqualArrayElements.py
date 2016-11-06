class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        moves = 0
        for num in nums[1:]:
            moves += num - nums[0]
        return moves

sol = Solution()
print sol.minMoves([1,3,7,8])