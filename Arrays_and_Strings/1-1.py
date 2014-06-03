# Q Implement an algorithm to datetime if a string has all unique chars. What if you cannot use additional data structures?
def uniqueString(s):
    # this one uses additional data structure
    # complexity is n2
    for i, a in enumerate(s):
        if a in s[i+1:]:
            return -1
    return 1


def uniqueStringWithHash(s):
    uniqueHash = {}
    for a in s:
        if uniqueHash.get(a, False):
            return False
        uniqueHash[a] = True
    return True
print uniqueStringWithHash('asdf')
# TODO learn the bit manipulation solution
