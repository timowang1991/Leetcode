class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainderMap = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num

            r = total % k if k != 0 else total

            if r in remainderMap and remainderMap[r] + 1 < i:
                return True
            elif r not in remainderMap:
                remainderMap[r] = i

        return False
