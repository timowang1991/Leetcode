class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        leftIdx = 0
        rightIdx = len(nums) - 1

        while rightIdx - leftIdx > 1:
            midIdx = (leftIdx + rightIdx) / 2
            if nums[midIdx] == target:
                return midIdx
            elif nums[midIdx] <= nums[leftIdx] and (target <= nums[midIdx] or target >= nums[leftIdx]):
                rightIdx = midIdx
            elif nums[midIdx] >= nums[rightIdx] and (target >= nums[midIdx] or target <= nums[rightIdx]):
                leftIdx = midIdx
            elif target <= nums[midIdx]:
                rightIdx = midIdx
            elif target >= nums[midIdx]:
                leftIdx = midIdx

        if nums[rightIdx] == target:
            return rightIdx
        elif nums[leftIdx] == target:
            return leftIdx

        return -1