# Q add two number stred as LinkedLists
from LinkedLists import LinkedList, Node


def add_numbers(l1, l2):
    if l1 == l2:
        return "I am not that smart or in other words I am a bit lazy"

    tmp1 = l1.head
    tmp2 = l2.head

    l3 = LinkedList()

    carry = 0
    while tmp1 and tmp2:
        crudeSum = tmp1.data + tmp2.data + carry
        sum = crudeSum % 10
        tmp3 = Node(sum)
        l3.insert_last(tmp3)

        carry = crudeSum / 10
        tmp1 = tmp1.next
        tmp2 = tmp2.next

    if tmp1:
        while tmp1:
            crudeSum = tmp1.data + carry
            sum = crudeSum % 10
            tmp3 = Node(sum)
            l3.insert_last(tmp3)

            carry = crudeSum / 10
            tmp1 = tmp1.next
    else:
        while tmp2:
            crudeSum = tmp2.data + carry
            sum = crudeSum % 10
            tmp3 = Node(sum)
            l3.insert_last(tmp3)

            carry = crudeSum / 10
            tmp2 = tmp2.next

    if carry:
        l3.insert_last(Node(carry))
    return l3


def main():
    l1 = LinkedList()
    l2 = LinkedList()
    [l1.insert_first(Node(0)) for i in range(0, 2)]
    [l2.insert_first(Node(1)) for i in range(0, 3)]
    print l1
    print l2
    print add_numbers(l1, l2)


if __name__ == '__main__':
    main()
