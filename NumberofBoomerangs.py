import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        numOfBoomerangs = 0
        for point1 in points:
            distances = {}

            for point2 in points:
                if point1 == point2:
                    continue
                distance = pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)
                if distance in distances:
                    distances[distance] += 1
                else:
                    distances[distance] = 1

            for distanceCnt in distances.itervalues():
                numOfBoomerangs += (ncr(distanceCnt, 2) * 2) if distanceCnt >= 2 else 0

        return numOfBoomerangs

sol = Solution()
print sol.numberOfBoomerangs([[5,5],[4,7],[6,5],[6,9],[3,7],[4,5],[2,5],[4,4],[3,0]])
