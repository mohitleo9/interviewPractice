from BST import Node, insert, search, levelOrder
import random


def ancestor(root, node1, node2, found1, found2, final):
    if not root:
        return
    if root == node1:
        found1[0] = True
    if root == node2:
        found2[0] = True

    ancestor(root.left, node1, node2, found1, found2, final)
    ancestor(root.right, node1, node2, found1, found2, final)

    if final[0]:
        return

    if found1[0] and found2[0]:
        ans = root
        final[0] = True
        print 'foundit!!!' + str(root)
        return ans


def main():
    root = Node(6)
    left = Node(4)
    right = Node(5)
    l1 = Node(3)
    l2 = Node(5)
    insert(left, l1)
    insert(left, l2)


    insert(root, left)
    insert(root, right)
    levelOrder(root)
    print ancestor(root, l1, l2, [False], [False], [False])
    print 'root is ' + str(left)


    pass


if __name__ == '__main__':
    main()
