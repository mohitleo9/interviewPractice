# given a sorted array create a BST
from BST import Node, insert, levelOrder


def createBstFromSorted(root, arr, start, end):
    if not root:
        return

    if start > end:
        root = None

        return
    mid = (start + end)/2
    root.data = Node(arr[mid])

    if not start > (mid - 1):
        root.left = Node()
        createBstFromSorted(root.left, arr, start, mid - 1)
    if not (mid + 1) > end:
        root.right = Node()
        createBstFromSorted(root.right, arr, mid + 1, end)


def main():
    root = Node()

    arr = [i for i in range(0, 7)]
    createBstFromSorted(root, arr, 0, len(arr)-1)
    levelOrder(root)

    print arr


if __name__ == '__main__':
    main()
