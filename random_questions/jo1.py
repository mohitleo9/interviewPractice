
def func_max_n(arr):
    sortedArr = arr.sort()
    sortedArr = arr

    val = -1

    for i in range(0, len(sortedArr) - 1):

        if ((len(sortedArr) - i - 1) >= sortedArr[i]) and sortedArr[i] > val:
            val = sortedArr[i]

    print 'output is ' + str(val)

def main():
    arr = [1,5,9,0,13,8,6,7,10]
    # arr = [900, 2, 901, 3, 1000]
    # arr = [1,2,3,4]
    func_max_n(arr)
    pass

if __name__ == '__main__':
    main()
