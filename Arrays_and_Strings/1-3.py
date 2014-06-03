# Q find out if a string is a permutation of the other
def isStrinPermuation(s1, s2):
    if len(s1) != len(s2):
        return False

    for s in s1:
        try:
            pos = s2.index(s)
        except Exception:
            return False
        del s2[pos]
    return True

print isStrinPermuation(list('asdf'), list('asdf'))
