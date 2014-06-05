# Q delete the duplicate nodes from a linked list (when no extra buffer is allowed)
from LinkedLists import LinkedList, Node


# naive approach
def remove_duplicates1(l, data):
    while l.delete_node(data):
        pass


def remove_duplicates(l, data):
    if not l.head:
        return
    tmp = l.head

    # handle the case when multiple datas are at the beginning of the list
    while tmp:
        if not tmp.data == data:
            break
        l.head = l.head.next
        tmp = tmp.next
    # now we can be confident that there is no node at the begining of the list
    # that matches the data
    while tmp.next:
        if tmp.next.data == data:
            tmp.next = tmp.next.next
            continue
        tmp = tmp.next


def main():
    l = LinkedList()
    [l.insert_last(Node(2)) for i in range(0, 3)]
    [l.insert_last(Node(i)) for i in range(0, 3)]
    print l
    remove_duplicates(l, 2)
    print l

if __name__ == '__main__':
    main()


