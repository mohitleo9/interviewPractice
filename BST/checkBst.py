from BST import Node, insert, levelOrder


def checkTree(root):
    if not root:
        return True

    if root.right:
        if root.right.data > root.data:
            return True and checkTree(root.right)
        else:
            return False
    if root.left:
        if root.left.data <= root.data:
            return True and checkTree(root.left)
        else:
            return False

    return True


def main():
    root = Node(2)
    insert(root, Node(3))
    levelOrder(root)
    print checkTree(root)
    pass


if __name__ == '__main__':
    main()
