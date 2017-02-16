inputString = list("This   is  a test")

def swapString(inputString, left, right):
    for i in xrange(left, (left+right)/2 + 1):
        tmp = inputString[i]
        inputString[i] = inputString[right - i + left]
        inputString[right - i + left] = tmp
        # print i, tmp, inputString[i], inputString[right - i]
    # print inputString

swapString(inputString, 0, len(inputString) - 1)
# swapString(inputString, 0, 2)

# for i, char in enumerate(inputString):
#     tmp = inputString[i]
#     inputString[i] = inputString[len(inputString) - i - 1]
#     inputString[len(inputString) - i - 1] = tmp

# print inputString

# print '\n\n\n'

left = 0
right = 0
for i, char in enumerate(inputString):
    if char == ' ':
        # print left, right
        swapString(inputString, left, right)
        left = i + 1
    else:
        right = i

swapString(inputString, left, right)

print ''.join(inputString)