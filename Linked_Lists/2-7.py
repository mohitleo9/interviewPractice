# Q palindrome string list
from LinkedLists import LinkedList, Node


def is_panildrome(l, first, last, hasLooped):
    # case where empty list

    if not last:
        hasLooped[0] = True
        return l.head

    first = is_panildrome(l, first, last.next, hasLooped)

    if hasLooped[0] and first not in [False, True]:
        if first.data != last.data:
            return False

        if first == last:
            return True

        first = first.next
    return first


def main():
    l = LinkedList()

    for i in ['1', '2', '3', '2', '1', '2']:
        l.insert_last(Node(i))

    print is_panildrome(l, l.head, l.head, [False])


if __name__ == '__main__':
    main()
