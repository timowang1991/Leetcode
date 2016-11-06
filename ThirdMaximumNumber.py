import heapq

class MaxHeapElem(object):
    def __init__(self, x):
        self.x = x
    def __cmp__(self, other):
        return -cmp(self.x, other.x)

def maxHeapPush(heap, x):
    heapq.heappush(heap, MaxHeapElem(x))

def maxHeapPop(heap):
    return heapq.heappop(heap).x

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxHeap = [MaxHeapElem(x) for x in nums]
        heapq.heapify(maxHeap)


        lastNum = maxHeapPop(maxHeap)
        maxNum = lastNum
        count = 1

        while(len(maxHeap) > 0 and count < 3):
            thisNum = maxHeapPop(maxHeap)

            if thisNum == lastNum:
                continue

            lastNum = thisNum
            count += 1

        if count < 3:
            return maxNum
        return lastNum

print Solution().thirdMax([1, 2, 3, 4, 4, 4])