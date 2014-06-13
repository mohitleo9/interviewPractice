from BST import Node, insert, levelOrder, height
import random


def list_level(root, level):
    if level < 0 or level > height(root) - 1:
        return
    if level == 0:
        print root
        return
    list_level(root.left, level - 1)
    list_level(root.right, level - 1)


def main():
    root = Node(1)
    insert(root, Node(0))
    insert(root, Node(2))
    for i in range(0, 9):
        insert(root, Node(random.randint(0, i)))
    levelOrder(root)
    print 'asdf'
    list_level(root, 3)
    pass

if __name__ == '__main__':
    main()
