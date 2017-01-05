class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
        wordSet.discard(beginWord)

        front, back = set([beginWord]), set([endWord])
        length = 2
        while len(front) > 0:
            front = wordSet & set(word[:i] + alph + word[i+1:] for word in front
                for i, char in enumerate(word) for alph in 'abcdefghijklmnopqrstuvwxyz')

            if front & back:
                return length

            length += 1

            if len(front) >= len(back):
                front, back = back, front

            wordSet -= front

        return 0


sol = Solution()
print sol.ladderLength('hit', 'cog', ['hot','dot','dog','lot','log'])