def isRotation(strina, strinb):
    newString = strina + strina
    if strinb in newString:
        return True
    else:
        return False

print isRotation('asdf', 'fasd')
