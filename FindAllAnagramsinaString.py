from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counter1 = Counter(p)
        counter2 = Counter(s[:len(p)-1])

        anagramIdxes = []

        for i in xrange(len(p)-1, len(s)):
            counter2[s[i]] += 1

            if counter1 == counter2:
                anagramIdxes.append(i - len(p) + 1)

            counter2[s[i - len(p) + 1]] -= 1
            if counter2[s[i - len(p) + 1]] == 0:
                del counter2[s[i - len(p) + 1]]

        return anagramIdxes

