# Q implement a BST
class Node:

    """This is Different Node for the Binary Search Tree"""

    def __init__(self, data=0):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return self.data


def insert(root, node, parent=None):
    if not root:
        root = node
        root.parent = parent
        return

    if node.data > root.data:
        if root.right:
            insert(root.right, node, root)
        else:
            root.right = node
            root.parent = parent
    else:
        if root.left:
            insert(root.left, node, root)
        else:
            root.left = node
            root.parent = parent


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.data
    inorder(root.right)


def main():
    root = Node(2)
    n = Node(3)
    insert(None, root)
    insert(root, n)
    insert(root, Node(5))

    inorder(root)

if __name__ == '__main__':
    main()
