# Q palindrome string list
from LinkedLists import LinkedList, Node


def is_panildrome(l, last):
    # case where empty list

    if not last:
        return l.head

    first = is_panildrome(l, last.next)

    if first not in [False, True]:
        if first.data != last.data:
            return False

        if first == last:
            return True

        first = first.next
    return first


def main():
    l = LinkedList()

    for i in ['1', '2', '3', '3', '1']:
        l.insert_last(Node(i))

    print is_panildrome(l, l.head)


if __name__ == '__main__':
    main()
