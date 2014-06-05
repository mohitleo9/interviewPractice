# Q return the kth to the last element 
from LinkedLists import LinkedList, Node


def k_to_last(l, k):
    if not l.head:
        return False
    runner = l.head

    pos = 0
    while runner and pos < k:
        pos += 1
        runner = runner.next

    if not pos == k:
        return False

    tmp = l.head

    while runner:
        tmp = tmp.next
        runner = runner.next

    return tmp


def k_recursive(n, k, count):
    if not n:
        count[0] = 0
        return False

    tll = k_recursive(n.next, k, count)
    count[0] += 1
    if k == count[0]:
        return n

    return tll


def main():
    l = LinkedList()
    for i in range(0, 10):
        l.insert_last(Node(i))

    print l
    # print k_to_last(l, 11)
    # print k_to_last(l, 8)

    k = 3
    count = [0]
    # notice that the head is passed not the list itself
    print k_recursive(l.head, k, count)


if __name__ == '__main__':
    main()

