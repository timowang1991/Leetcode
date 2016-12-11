class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorderInArr = preorder.split(',')
        stack = []

        for node in preorderInArr:
            stack.append(node)
            while len(stack) >= 2 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                try:
                    stack[-1] = '#'
                except Exception as e:
                    return False

        return True if len(stack) == 1 and stack[0] == '#' else False

sol = Solution()
print sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print sol.isValidSerialization("1,#")
print sol.isValidSerialization("9,#,#,1")
print sol.isValidSerialization("1,#,#,#,#")