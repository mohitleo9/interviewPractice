def compressString(string):
    count = 1
    last = string[0]
    newString = ''
    for i in range(1, len(string)):
        if string[i] == last:
            count += 1
            continue

        newString = newString + last + str(count)
        count = 1
        last = string[i]
    newString = newString + last + str(count)
    if len(newString) > len(string):
        return string
    else:
        return newString

print compressString('asddf')
