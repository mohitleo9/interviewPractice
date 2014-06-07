import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Linked_Lists.LinkedLists import LinkedList, Node


class Stack:
    def push(self, node):
        if not node:
            return

        if not self.top:
            self.top = node
            return
        node.next = self.top
        self.top = node
        return

    def pop(self):
        if not self.top:
            return
        tmp = self.top
        self.top = self.top.next

        return tmp

    def peek(self):
        return self.top.data

    def __init__(self):
        self.top = None

    def __str__(self):
        if not self.top:
            return "None"

        tmp = self.top
        strin = ''
        while tmp.next:
            strin += str(tmp.data) + '->'
            tmp = tmp.next

        strin += str(tmp.data) + '->'
        strin += 'None'
        return strin



def main():
    s = Stack()
    s.push(Node(2))
    s.push(Node(3))
    s.pop()
    s.pop()
    print s

if __name__ == '__main__':
    main()
