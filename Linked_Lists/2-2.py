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


def main():
    l = LinkedList()
    for i in range(0, 10):
        l.insert_last(Node(i))

    print l
    print k_to_last(l, 11)
    print k_to_last(l, 8)


if __name__ == '__main__':
    main()

