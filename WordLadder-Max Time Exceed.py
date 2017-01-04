class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordSet = set()
        length = 0
        for word in wordList:
            wordSet.add(word)

        paths = [{'lastWord': beginWord, 'collectedWordSet': set()}]

        change = True
        while change:
            change = False
            nextPaths = []
            for path in paths:
                lastWord = path['lastWord']
                for i, char in enumerate(lastWord):
                    for alph in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = lastWord[:i] + alph + lastWord[i+1:]
                        if newWord == endWord:
                            return len(path['collectedWordSet']) + 2
                        if newWord in wordSet and newWord not in path['collectedWordSet']:
                            # print 'newWord', newWord, "path['collectedWordSet]", path['collectedWordSet']
                            change = True
                            nextPaths.append({ 'lastWord': newWord, 'collectedWordSet': path['collectedWordSet'] | set([newWord]) })
            paths = nextPaths
        return 0


sol = Solution()
print sol.ladderLength('hit', 'cog', ['hot','dot','dog','lot','log'])