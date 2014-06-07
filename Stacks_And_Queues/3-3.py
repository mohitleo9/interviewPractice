# Q implement stack of stacks
from Stack import *


class StackOfStacks:
    def __init__(self, max_length=3):
        self.max_length = max_length
        # stack refers to the index of the stackArray
        self.stackindex = None
        self.stackArray = []
        self.length = 0

    def push(self, node):
        if self.stackindex == None:
            self.stackindex = 0
            tmp = Stack()
            tmp.push(node)
            self.stackArray.append(tmp)
            self.length += 1
            return

        # if current stack has space
        if (self.length % self.max_length) != 0:
            self.stackArray[self.stackindex].push(node)
        else:
            tmp = Stack()
            tmp.push(node)
            self.stackindex += 1
            self.stackArray.append(tmp)

        self.length += 1

    def pop(self):
        if self.stackindex == None:
            return
        if self.length % self.max_length > 1:
            self.stackArray[self.stackindex].pop()
        else:
            self.stackArray[self.stackindex].pop()
            del self.stackArray[self.stackindex]
            self.stackindex -= 1
        self.length -= 1

    def __str__(self):
        if self.length == 0:
            return 'None'
        string = ''
        for i in range(0, self.stackindex + 1):
            string += str(self.stackArray[i])
        return string


def main():
    s = StackOfStacks(2)
    s.push(Node(9))
    s.push(Node(10))
    s.push(Node(11))
    s.push(Node(12))
    s.push(Node(13))
    print s

    s.pop()
    print s

if __name__ == '__main__':
    main()
