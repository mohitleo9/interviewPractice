# Q9.1
def count_steps(n, sol={}):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif sol.get(n, False):
        return sol[n]
    else:
        sol[n] = count_steps(n-1) + count_steps(n-2) + count_steps(n-3)
        return sol[n]


def main():
    print count_steps(8)


if __name__ == '__main__':
    main()
