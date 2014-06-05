class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, node):
        if not node:
            return
        if not self.head:
            self.head = node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        # insert node
        tmp.next = node

    def delete_node(self, data):
        if not self.head:
            return False

        tmp = self.head
        if tmp.data == data:
            self.head = self.head.next
            return True

        found = False
        while tmp.next:
            if tmp.next.data == data:
                found = True
                break
            tmp = tmp.next

        if not found:
            return False
        tmp.next = tmp.next.next
        return True

    def __str__(self):
        if not self.head:
            return "None"

        tmp = self.head
        strin = ''
        while tmp.next:
            strin += str(tmp.data) + '->'
            tmp = tmp.next

        strin += str(tmp.data) + '->'
        strin += 'None'
        return strin


def main():
    n = Node(2)
    l = LinkedList()
    l.insert_last(n)
    n = Node(4)
    l.insert_last(n)
    n = Node(5)
    l.insert_last(n)
    n = Node(6)
    l.insert_last(n)
    print l.delete_node(2)
    print l.delete_node(6)
    print l.delete_node(4)
    print l
if __name__ == '__main__':
    main()




