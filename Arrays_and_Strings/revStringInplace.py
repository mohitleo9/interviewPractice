
def revString(string):
    if string:
        start = string[0]
    else:
        return

    if len(string) > 1:
        last = revString(string[1:])
        start, last = last, start
        return last
    return start


def main():
    arr = []
    for s in 'string':
        arr.append(s)
    print arr
    print revString(arr)
    print arr



if __name__ == '__main__':
    main()
