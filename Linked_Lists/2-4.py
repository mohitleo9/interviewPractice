import random
from LinkedLists import LinkedList, Node


# does not handle if the number itself is in the list 
# cuz it is really trivial
def rearrange(l, data):
    if not l.head:
        return False

    # append an extra node at the front to handle the special case
    # of head greater than data
    tmpList = LinkedList()
    tmp = l.head
    while tmp:
        if tmp.data < data:
            # delete tmp.next
            # tmptmp = tmp.next
            # tmp.next = tmp.next.next
            # insert the deleted node at begining
            tmpList.insert_first(Node(tmp.data))
        if tmp.data >= data:
            # delete tmp.next
            # tmptmp = tmp.next
            # tmp.next = tmp.next.next
            # insert the deleted node at end
            tmpList.insert_last(Node(tmp.data))

        tmp = tmp.next

    return tmpList


def main():
    l = LinkedList()
    for i in range(0, 8):
        l.insert_last(Node(random.randint(0, 7)))

    print l
    print rearrange(l, 4)
    pass

if __name__ == '__main__':
    main()
