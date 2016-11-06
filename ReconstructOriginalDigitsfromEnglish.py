{
    '0': 'zero',    #z
    '1': 'one',         #o
    '2': 'two',     #w
    '3': 'three',       #h
    '4': 'four',    #u
    '5': 'five',        #f
    '6': 'six',     #x
    '7': 'seven',           #s
    '8': 'eight',   #g
    '9': 'nine'             #i
}

priority1 = {'z':('zero', 0), 'w':('two', 2), 'u':('four', 4), 'x':('six', 6), 'g':('eight', 8)}
priority2 = {'o':('one', 1), 'h':('three', 3), 'f':('five', 5)}
priority3 = {'s':('seven', 7), 'i':('nine', 9)}
priorities = [priority1, priority2, priority3]

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cutOutStrings = list(s)
        digits = []
        deleteStrCnt = {}

        j = 0
        while j < len(priorities):
            priority = priorities[j]
            for i, c in enumerate(cutOutStrings):
                if c in priority:
                    delCharStr, digit = priority[c]

                    for delChar in delCharStr:
                        if delChar in deleteStrCnt:
                            deleteStrCnt[delChar] += 1
                        else:
                            deleteStrCnt[delChar] = 1

                    digits.append(digit)
                    # print deleteStrCnt

                if c in deleteStrCnt and deleteStrCnt[c] > 0:
                    cutOutStrings[i] = None
                    deleteStrCnt[c] -= 1

            if all(value == 0 for value in deleteStrCnt.values()):
                j += 1

        return ''.join(str(d) for d in sorted(digits))

sol = Solution();
print sol.originalDigits('fviefuro')