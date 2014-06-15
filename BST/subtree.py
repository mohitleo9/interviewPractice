from BST import insert, levelOrder, Node
from insert_sorted import createBstFromSorted


def match(root1, root2):
    # if the second if finished
    if not root2:
        return True
    if not root1:
        return False
    if root1.data == root2.data:
        left = match(root1.left, root2.left)
        right = match(root1.right, root2.right)
        return left and right
    else:
        return False


def subtree(root1, root2):
    if not root1:
        return False
    if root1.data == root2.data:
        print 'oh '
        if match(root1, root2):
            return True
    else:
        left = subtree(root1.left, root2)
        right = subtree(root1.right, root2)
        return left or right


def main():
    root1 = Node(0)
    root2 = Node(10)
    insert(root2, Node(5))
    insert(root2, Node(7))
    arr = [i for i in range(0, 9)]
    createBstFromSorted(root1, arr, 0, len(arr)-1)

    levelOrder(root1)
    print 'root2'
    levelOrder(root2)

    print subtree(root1, root2)

    pass


if __name__ == '__main__':
    main()
