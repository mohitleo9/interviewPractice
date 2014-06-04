# Q replace all the occurances of space in a string with '%20'
def replaceSpace(list, sub):
    asdf = sub.join(list.split(' '))
    print asdf


replaceSpace(' asdf asdf  asdf  ', '111')
