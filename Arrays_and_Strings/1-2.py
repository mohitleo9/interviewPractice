# Q reverse a string in place
def reverseString(s):
    revLen = len(s)/2
    print revLen
    for i in range(0, revLen):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]


reverseString(list('alsf'))
